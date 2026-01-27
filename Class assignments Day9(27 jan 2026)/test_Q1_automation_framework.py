
import pytest
import configparser

config_data = """
[DEFAULT]
app_name = Sample Automation Framework
environment = test
"""

config = configparser.ConfigParser()
config.read_string(config_data)

def add(a, b):
    """Simple function to validate"""
    return a + b


@pytest.fixture
def app_config():
    return config["DEFAULT"]

def test_addition(app_config):
    print("Application:", app_config["app_name"])
    print("Environment:", app_config["environment"])
    result = add(2, 3)
    assert result == 5

def test_addition_negative():
    result = add(-1, -1)
    assert result == -2
