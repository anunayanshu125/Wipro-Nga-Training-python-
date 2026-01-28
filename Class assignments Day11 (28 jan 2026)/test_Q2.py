import pytest

def login(username, password):
    if username == "admin" and password == "admin123":
        return True
    return False

def add_to_cart(is_logged_in, product):
    if is_logged_in and product:
        return "Product added"
    return "Action failed"

def checkout(cart_status):
    if cart_status == "Product added":
        return "Order placed"
    return "Checkout failed"

def test_successful_order_flow():
    """
    End-to-end test:
    Login -> Add to cart -> Checkout
    """
    logged_in = login("admin", "admin123")
    cart = add_to_cart(logged_in, "Laptop")
    result = checkout(cart)
    assert result == "Order placed"


def test_order_without_login():
    """
    End-to-end failure scenario
    """
    logged_in = login("user", "wrong")
    cart = add_to_cart(logged_in, "Laptop")
    result = checkout(cart)
    assert result == "Checkout failed"


def test_empty_cart_checkout():
    """
    Edge case functional test
    """
    logged_in = login("admin", "admin123")
    cart = add_to_cart(logged_in, "")
    result = checkout(cart)
    assert result == "Checkout failed"

@pytest.mark.xfail(reason="Known issue: checkout fails intermittently")
def test_known_checkout_issue():
    logged_in = login("admin", "admin123")
    cart = add_to_cart(logged_in, "Phone")
    result = checkout(cart)
    assert result == "Order placed"