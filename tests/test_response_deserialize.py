import json
from unittest.mock import MagicMock, patch

import ynab
from ynab.api.transactions_api import TransactionsApi
from ynab.api_client import ApiClient
from ynab.rest import RESTResponse


def make_rest_response(status, body_dict):
    """Build a RESTResponse from a status code and JSON-serializable dict."""
    resp = MagicMock()
    resp.status = status
    resp.reason = "OK"
    resp.headers = {"content-type": "application/json; charset=utf-8"}
    resp.data = json.dumps(body_dict).encode("utf-8")

    rest_resp = RESTResponse(resp)
    rest_resp.read()
    return rest_resp


def test_deserialize_user_response():
    """Exercises the full RESTResponse -> api_client.response_deserialize path.

    This would have caught the .headers vs .getheaders() mismatch.
    """
    client = ApiClient()
    rest_resp = make_rest_response(200, {
        "data": {"user": {"id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"}}
    })

    result = client.response_deserialize(
        response_data=rest_resp,
        response_types_map={"200": "UserResponse"},
    )

    assert result.status_code == 200
    assert str(result.data.data.user.id) == "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"


def test_update_transactions_with_http_info_deserializes_real_200_response():
    """Regression test: TransactionsApi.update_transactions must map status
    200, not 209, in its own generated _response_types_map.

    The spec previously declared updateTransactions' success response as
    HTTP 209, but the real API returns 200. Since 200 didn't match the
    hardcoded map inside update_transactions/_with_http_info/
    _without_preload_content, every real, successful call silently
    deserialized to data=None -- callers had no way to tell the request
    had in fact succeeded. This calls the real generated method (not a
    hand-supplied response_types_map) so it actually exercises the fixed
    value embedded in transactions_api.py.
    """
    client = ApiClient()
    rest_resp = make_rest_response(200, {
        "data": {
            "transaction_ids": ["aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"],
            "transactions": [],
            "duplicate_import_ids": [],
            "server_knowledge": 1,
        }
    })

    with patch.object(ApiClient, "call_api", return_value=rest_resp):
        api = TransactionsApi(client)
        result = api.update_transactions_with_http_info(
            plan_id="last-used",
            data=ynab.PatchTransactionsWrapper(transactions=[]),
        )

    assert result.status_code == 200
    assert result.data is not None
    assert result.data.data.transaction_ids == [
        "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
    ]
