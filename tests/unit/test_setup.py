import os

import pytest

from cloudcraftco.cloudcraft import Cloudcraft


def test_config_default_setup():
    """Test default values returned by config."""
    defaults_with_key = {
        "api_key": "uuid",
        "host": "api.cloudcraft.co",
        "max_network_retries": 10,
        "port": 443,
        "protocol": "https",
        "timeout": 80000,
    }
    cloudcraft = Cloudcraft({"api_key": "uuid"})

    assert cloudcraft.config == defaults_with_key


def test_config_url_base():
    """Test handling of missing port config."""
    config = {
        "api_key": "uuid",
        "host": "host.io",
        "max_network_retries": 10,
        "port": None,
        "protocol": "https",
        "timeout": 80000,
    }
    cloudcraft = Cloudcraft(config)

    assert cloudcraft.url_base == "https://host.io{}"


def test_config_env_setup():
    """Test config defined in environment."""
    fixture = {
        "api_key": "uuid",
        "host": "api.host.io",
        "max_network_retries": 44,
        "port": 3333,
        "protocol": "http",
        "timeout": 888,
    }
    os.environ["CLOUDCRAFT_API_KEY"] = fixture["api_key"]
    os.environ["CLOUDCRAFT_HOST"] = fixture["host"]
    os.environ["CLOUDCRAFT_MAX_NETWORK_RETRIES"] = str(fixture["max_network_retries"])
    os.environ["CLOUDCRAFT_PORT"] = str(fixture["port"])
    os.environ["CLOUDCRAFT_PROTOCOL"] = fixture["protocol"]
    os.environ["CLOUDCRAFT_TIMEOUT"] = str(fixture["timeout"])
    cloudcraft = Cloudcraft()

    assert cloudcraft.config == fixture


def test_config_api_key_exists():
    """Test error thrown for missing api key."""
    del os.environ["CLOUDCRAFT_API_KEY"]
    with pytest.raises(Exception) as e_info:
        cloudcraft = Cloudcraft()
