import pytest

from cloudcraftco.cloudcraft import Cloudcraft

# Warning: testing against production
# api_key must be assigned to env-variable

cloudcraft = Cloudcraft()


def test_user_api():
    """Test api response for read_user_profile."""
    profile = cloudcraft.read_user_profile()
    assert len(profile.get("id")) == 36
    assert profile.get("name") != None
    assert profile.get("email") != None
    assert profile.get("settings") != None
