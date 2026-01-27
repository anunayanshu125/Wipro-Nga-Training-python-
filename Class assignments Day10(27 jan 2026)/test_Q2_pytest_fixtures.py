import pytest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero not allowed")
    return a / b

def setup_module(module):
    print("\n[setup_module] Module setup")

def teardown_module(module):
    print("\n[teardown_module] Module teardown")

def setup_function(function):
    print("\n[setup_function] Before test")

def teardown_function(function):
    print("\n[teardown_function] After test")

@pytest.fixture(scope="function")
def numbers():
    return (10, 5)

@pytest.fixture(scope="module")
def shared_resource():
    print("\n[Fixture Setup] Opening resource")
    yield "RESOURCE"
    print("\n[Fixture Teardown] Closing resource")

def test_addition(numbers, shared_resource):
    a, b = numbers
    assert add(a, b) == 15

def test_division(numbers):
    a, b = numbers
    assert divide(a, b) == 2

def test_division_by_zero(shared_resource):
    with pytest.raises(ValueError):
        divide(10, 0)