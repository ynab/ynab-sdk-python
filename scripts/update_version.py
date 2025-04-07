#!/usr/bin/env python3
import sys
import subprocess
import re

def get_current_version():
    """Get the current version from poetry without bumping it."""
    result = subprocess.run(["poetry", "version", "-s"], capture_output=True, text=True)
    return result.stdout.strip()

def bump_poetry_version(bump_type):
    """Bump the poetry version with the specified bump type."""
    subprocess.run(["poetry", "version", "--quiet", bump_type], check=True)
    return get_current_version()

def update_openapi_config(version):
    """Update the packageVersion in the openapi-generator-config.yaml file."""
    config_file = "openapi-generator-config.yaml"
    
    # Read the current config file
    with open(config_file, 'r') as f:
        content = f.read()
    
    # Update the packageVersion line
    updated_content = re.sub(
        r'packageVersion:\s*.*', 
        f'packageVersion: {version}', 
        content
    )
    
    # Write the updated content back to the file
    with open(config_file, 'w') as f:
        f.write(updated_content)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <bump_type>")
        print("Example: patch|minor|major|1.4.1")
        sys.exit(1)
    
    bump_type = sys.argv[1]
    
    # Bump the version in pyproject.toml
    version = bump_poetry_version(bump_type)    
    
    # Update the version in openapi-generator-config.yaml
    update_openapi_config(version)
    print(f"{version}")    

if __name__ == "__main__":
    main()