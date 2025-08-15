import pytest
import jsonschema

pytestmark = [pytest.mark.api, pytest.mark.smoke]

PRODUCT_LIST_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["id", "title", "price"],
        "properties": {
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "price": {"type": "number"}
        }
    }
}

def test_products_list_schema(api_client) -> None:
    """
    Test that the products API returns a list of products matching the expected schema.

    Args:
        api_client: An instance of ApiClient fixture for making API requests.

    Returns:
        None

    Raises:
        AssertionError: If the response status is not 200, the schema does not match,
                        or the returned list is empty.
    """
    resp = api_client.get_products()
    assert resp.status_code == 200
    data = resp.json()
    jsonschema.validate(instance=data, schema=PRODUCT_LIST_SCHEMA)
    assert len(data) > 0
