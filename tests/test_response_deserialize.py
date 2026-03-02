import json
from unittest.mock import MagicMock

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
