from flask import Blueprint, jsonify, request

from app.utils.decorators import require_token
from app.utils.validators import validate_product
from app.utils.errors import APIError

from app.services.product_service import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product
)


product_bp = Blueprint("products", __name__)


@product_bp.route("/products", methods=["GET"])
def get_products():

    products = get_all_products()

    return jsonify([
        dict(product)
        for product in products
    ])


@product_bp.route("/products", methods=["POST"])
@require_token
def add_product():

    data = request.get_json()

    if not data:
        raise APIError(
            "JSON data required",
            400
        )

    name = data.get("name")
    price = data.get("price")

    error = validate_product(name, price)

    if error:
        raise APIError(
            error,
            400
        )

    try:
        price = float(price)

    except (ValueError, TypeError):

        raise APIError(
            "Price must be a number",
            400
        )

    new_id = create_product(name, price)

    return jsonify({
        "message": "Product added successfully",
        "id": new_id,
        "name": name,
        "price": price
    }), 201
    
@product_bp.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):

    product = get_product_by_id(product_id)

    if product is None:
        raise APIError(
            "Product not found",
            404
        )

    return jsonify({
        "id": product["id"],
        "name": product["name"],
        "price": product["price"]
    }), 200


@product_bp.route("/products/<int:product_id>", methods=["PUT"])
@require_token
def edit_product(product_id):

    data = request.get_json()

    if not data:
        raise APIError(
            "JSON data required",
            400
        )

    name = data.get("name")
    price = data.get("price")

    error = validate_product(name, price)

    if error:
        raise APIError(
            error,
            400
        )

    try:
        price = float(price)

    except (ValueError, TypeError):

        raise APIError(
            "Price must be a number",
            400
        )

    updated = update_product(
        product_id,
        name,
        price
    )

    if updated == 0:
        raise APIError(
            "Product not found",
            404
        )

    return jsonify({
        "message": "Product updated successfully",
        "id": product_id,
        "name": name,
        "price": price
    }), 200


@product_bp.route("/products/<int:product_id>", methods=["DELETE"])
@require_token
def remove_product(product_id):

    deleted = delete_product(product_id)

    if deleted == 0:
        raise APIError(
            "Product not found",
            404
        )

    return jsonify({
        "message": "Product deleted successfully"
    }), 200