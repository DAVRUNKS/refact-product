from app.utils.validators import validate_product


def test_valid_product():
    result = validate_product("Mouse", 25)

    assert result is None


def test_product_without_name():
    result = validate_product("", 25)

    assert result == "Name is required"


def test_product_without_price():
    result = validate_product("Mouse", None)

    assert result == "Price is required"


def test_product_with_invalid_price():
    result = validate_product("Mouse", "hello")

    assert result == "Price must be a number"


def test_product_with_negative_price():
    result = validate_product("Mouse", -10)

    assert result == "Price cannot be negative"