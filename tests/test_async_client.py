from unittest.mock import patch

import httpx
import pytest
import ynab

from ynab.async_api.user_api import AsyncUserApi
from ynab.async_api_client import AsyncApiClient
from ynab.async_rest import RESTResponse


@pytest.fixture
def user_response_body():
    return {"data": {"user": {"id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"}}}


@pytest.fixture
def async_rest_response(user_response_body):
    response = httpx.Response(200, json=user_response_body, headers={"content-type": "application/json; charset=utf-8"})
    return RESTResponse(response)


def test_async_exports():
    assert ynab.AsyncApiClient is AsyncApiClient
    assert ynab.AsyncUserApi is AsyncUserApi


@pytest.mark.asyncio
async def test_async_deserialize_user_response(async_rest_response):
    client = AsyncApiClient()
    await async_rest_response.read()

    result = client.response_deserialize(
        response_data=async_rest_response,
        response_types_map={"200": "UserResponse"},
    )

    assert result.status_code == 200
    assert str(result.data.data.user.id) == "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"


@pytest.mark.asyncio
@patch.object(AsyncApiClient, "call_api", autospec=True)
async def test_async_get_user_awaits_client_call(call_api, async_rest_response):
    call_api.return_value = async_rest_response
    client = AsyncApiClient()
    api = AsyncUserApi(client)

    result = await api.get_user()

    assert str(result.data.user.id) == "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
    call_api.assert_awaited_once()


@pytest.mark.asyncio
@patch.object(AsyncApiClient, "close", autospec=True)
async def test_async_context_manager_returns_client_and_closes(close):
    client = AsyncApiClient()

    async with client as context_client:
        assert context_client is client
        close.assert_not_awaited()

    close.assert_awaited_once_with(client)


@pytest.mark.asyncio
@patch.object(AsyncApiClient, "close", autospec=True)
async def test_async_context_manager_closes_when_block_raises(close):
    client = AsyncApiClient()

    with pytest.raises(RuntimeError, match="boom"):
        async with client:
            raise RuntimeError("boom")

    close.assert_awaited_once_with(client)


@pytest.mark.asyncio
@patch.object(AsyncApiClient, "call_api", autospec=True)
@patch.object(AsyncApiClient, "close", autospec=True)
async def test_async_api_call_inside_context_passes_request_options(close, call_api, async_rest_response):
    call_api.return_value = async_rest_response

    async with AsyncApiClient(header_name="X-Client", header_value="client-header") as client:
        api = AsyncUserApi(client)
        result = await api.get_user_with_http_info(_request_timeout=12.5, _headers={"X-Trace": "trace-id"})

    assert result.status_code == 200
    assert str(result.data.data.user.id) == "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
    close.assert_awaited_once_with(client)
    call_api.assert_awaited_once()

    call_args = call_api.await_args
    assert call_args.args[0] is client
    assert call_args.args[1] == "GET"
    assert call_args.args[2].endswith("/user")
    assert call_args.kwargs == {"_request_timeout": 12.5}
    assert call_args.args[3] == {
        "X-Trace": "trace-id",
        "Accept": "application/json",
        "User-Agent": "OpenAPI-Generator/4.1.0/python",
        "X-Client": "client-header",
    }
    assert call_args.args[4] is None
    assert call_args.args[5] == []


@pytest.mark.asyncio
@patch.object(AsyncApiClient, "call_api", autospec=True)
@patch.object(AsyncApiClient, "close", autospec=True)
async def test_async_without_preload_content_returns_raw_response_without_reading(close, call_api, async_rest_response):
    call_api.return_value = async_rest_response

    async with AsyncApiClient() as client:
        api = AsyncUserApi(client)
        response = await api.get_user_without_preload_content()

    assert response is async_rest_response.response
    assert async_rest_response.data is None
    close.assert_awaited_once_with(client)
