from app.services.product_service import (
    get_all_products,
    create_product
)


def test_create_product():

    product_id = create_product(
        "Test Mouse",
        25
    )

    assert product_id is not None


def test_get_all_products():

    create_product("Keyboard", 50)

    products = get_all_products()

    assert len(products) >= 1