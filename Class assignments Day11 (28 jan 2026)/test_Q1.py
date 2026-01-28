import pytest
import sys

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests (dev/prod)"
    )
@pytest.fixture
def env(request):
    try:
        return request.config.getoption("env")
    except Exception:
        return "dev"


# -------------------------------------------------
# Function to test
# -------------------------------------------------

def add(a, b):
    return a + b
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (10, 20, 30),
        (-1, 1, 0)
    ]
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

def test_environment_selection(env):
    assert env in ["dev", "prod"]

@pytest.mark.skip(reason="Feature under development")
def test_future_feature():
    assert True

@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_only():
    assert True

@pytest.mark.xfail(reason="Known bug in calculation")
def test_known_bug():
    assert add(2, 2) == 5