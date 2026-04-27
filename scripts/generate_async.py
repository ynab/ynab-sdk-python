#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


API_CLASS_RE = re.compile(r"\b([A-Z][A-Za-z0-9]+Api)\b")
API_IMPORT_RE = re.compile(r"from ynab\.api\.([a-z_]+_api) import ([A-Z][A-Za-z0-9]+Api) as \2")


def async_class_name(name: str) -> str:
    return name if name.startswith("Async") else f"Async{name}"


def transform_api_text(text: str) -> str:
    text = text.replace("from ynab.api_client import ApiClient, RequestSerialized", "from ynab.async_api_client import AsyncApiClient, RequestSerialized")
    text = text.replace("from ynab.rest import RESTResponseType", "from ynab.async_rest import RESTResponseType")
    text = text.replace("ApiClient.get_default()", "AsyncApiClient.get_default()")
    text = API_CLASS_RE.sub(lambda match: async_class_name(match.group(1)), text)
    return text


def transform_api_client_text(text: str) -> str:
    text = text.replace("from ynab import rest", "from ynab import async_rest as rest")
    text = text.replace("class ApiClient:", "class AsyncApiClient:")
    text = text.replace("ApiClient()", "AsyncApiClient()")
    text = text.replace("object of ApiClient class", "object of AsyncApiClient class")
    text = text.replace("The ApiClient object.", "The AsyncApiClient object.")
    text = text.replace(":param default: object of ApiClient.", ":param default: object of AsyncApiClient.")
    return text


def transform_rest_text(text: str) -> str:
    text = text.replace("cadata=configuration.ca_cert_data,", 'cadata=getattr(configuration, "ca_cert_data", None),')
    return text


def write_async_api_init(api_files: list[Path], target: Path) -> None:
    lines = ["# flake8: noqa", "", "# import async apis into async_api package"]
    for api_file in api_files:
        class_name = async_class_name("".join(part.title() for part in api_file.stem.removesuffix("_api").split("_")) + "Api")
        lines.append(f"from ynab.async_api.{api_file.stem} import {class_name}")
    target.write_text("\n".join(lines) + "\n")


def patch_package_init(package_init: Path, api_files: list[Path]) -> None:
    text = package_init.read_text()
    api_imports = API_IMPORT_RE.findall(text)
    async_names = [async_class_name(class_name) for _, class_name in api_imports]

    for async_name in async_names:
        entry = f'    "{async_name}",'
        if entry not in text:
            text = text.replace('    "ApiResponse",', f"{entry}\n    \"ApiResponse\",")

    if '    "AsyncApiClient",' not in text:
        text = text.replace('    "ApiClient",', '    "ApiClient",\n    "AsyncApiClient",')

    async_import_lines = []
    for module_name, class_name in api_imports:
        async_name = async_class_name(class_name)
        async_import_lines.append(f"from ynab.async_api.{module_name} import {async_name} as {async_name}")
    async_imports = "\n".join(async_import_lines)
    marker = "# import ApiClient"
    if async_imports not in text:
        text = text.replace(marker, f"{async_imports}\n\n{marker}")

    async_client_import = "from ynab.async_api_client import AsyncApiClient as AsyncApiClient"
    if async_client_import not in text:
        text = text.replace("from ynab.api_client import ApiClient as ApiClient", f"from ynab.api_client import ApiClient as ApiClient\n{async_client_import}")

    package_init.write_text(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("generated_dir", type=Path)
    parser.add_argument("--package-dir", type=Path, default=Path("ynab"))
    args = parser.parse_args()

    source_package = args.generated_dir / "ynab"
    target_package = args.package_dir
    async_api_dir = target_package / "async_api"
    async_api_dir.mkdir(parents=True, exist_ok=True)

    api_files = sorted((source_package / "api").glob("*_api.py"))
    for api_file in api_files:
        (async_api_dir / api_file.name).write_text(transform_api_text(api_file.read_text()))

    write_async_api_init(api_files, async_api_dir / "__init__.py")
    (target_package / "async_api_client.py").write_text(transform_api_client_text((source_package / "api_client.py").read_text()))
    (target_package / "async_rest.py").write_text(transform_rest_text((source_package / "rest.py").read_text()))
    shutil.copyfile(source_package / "py.typed", target_package / "py.typed")
    patch_package_init(target_package / "__init__.py", api_files)


if __name__ == "__main__":
    main()
