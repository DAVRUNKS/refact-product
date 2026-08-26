def validate_product(name, price):

    if not name:
        return "Name is required"

    if price is None:
        return "Price is required"

    try:
        price = float(price)
    except (ValueError, TypeError):
        return "Price must be a number"

    if price < 0:
        return "Price cannot be negative"

    return None


def validate_registration(username, password):

    if not username:
        return "Username is required"

    if not password:
        return "Password is required"

    if len(password) < 6:
        return "Password must be at least 6 characters"

    return None

def validate_product(name, price):

    if not name:
        return "Name is required"

    if price is None:
        return "Price is required"

    try:
        price = float(price)
    except (ValueError, TypeError):
        return "Price must be a number"

    if price < 0:
        return "Price cannot be negative"

    return None


def validate_registration(username, password):

    if not username:
        return "Username is required"

    if not password:
        return "Password is required"

    if len(password) < 6:
        return "Password must be at least 6 characters"

    return None