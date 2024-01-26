import pytest

from cloudcraftco.cloudcraft import Cloudcraft


@pytest.fixture()
def read_user_profile_fixture():
    fixture = {
        "id": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
        "name": "Example API User",
        "email": "user@example.org",
        "settings": {"key": "value, Cloudcraft UI settings"},
        "createdAt": "2022-01-01T20:54:47.282Z",
        "updatedAt": "2022-01-01T20:54:53.963Z",
    }
    return fixture


def test_read_user_profile(mocker, read_user_profile_fixture):
    """Test read_user_profile handler."""
    fake_resp = mocker.Mock()
    fake_resp.json = mocker.Mock(return_value=read_user_profile_fixture)
    fake_resp.status_code = 200
    mocker.patch("requests.get", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    profile = cloudcraft.read_user_profile()

    assert profile == fake_resp.json()
