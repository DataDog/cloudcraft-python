import pytest

from cloudcraftco.cloudcraft import Cloudcraft


def test_get_account():
    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    with pytest.raises(Exception) as e_info:
        account = cloudcraft.read_aws_account("uuid")


@pytest.fixture()
def error_fixture():
    fixture = {
        "error": "Very regrettable situation.",
    }
    return fixture


def test_unexpected_response(mocker, error_fixture):
    """Test unexpected api response."""
    fake_resp = mocker.Mock()
    fake_resp.status_code = 418
    fake_resp.json = mocker.Mock(return_value=error_fixture)
    mocker.patch("requests.get", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "invalid", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    with pytest.raises(Exception) as e_info:
        account = cloudcraft.list_aws_accounts()
    message = e_info.value
    assert str(e_info.value).startswith("Undocumented Response.")


def test_malformed_response(mocker, error_fixture):
    """Test malformed api response."""
    fake_resp = mocker.Mock()
    fake_resp.status_code = 400
    fake_resp.json = mocker.Mock(return_value=error_fixture)
    mocker.patch("requests.delete", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "invalid", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    with pytest.raises(Exception) as e_info:
        account = cloudcraft.delete_aws_account("invalid-id")
    assert str(e_info.value).startswith("Malformed request.")


def test_unauthorized_response(mocker, error_fixture):
    """Test unauthorized api response."""
    fake_resp = mocker.Mock()
    fake_resp.status_code = 401
    fake_resp.json = mocker.Mock(return_value=error_fixture)
    mocker.patch("requests.get", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "invalid", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    with pytest.raises(Exception) as e_info:
        account = cloudcraft.list_aws_accounts()
    assert str(e_info.value).startswith("Unauthorized request.")


def test_forbidden_response(mocker, error_fixture):
    """Test forbidden api response."""
    fake_resp = mocker.Mock()
    fake_resp.status_code = 403
    fake_resp.json = mocker.Mock(return_value=error_fixture)
    mocker.patch("requests.post", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "invalid", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    with pytest.raises(Exception) as e_info:
        account = cloudcraft.create_aws_account({"ignore": "me"})
    assert str(e_info.value).startswith("Forbidden, insufficient priviledges.")


def test_missing_resource_response(mocker, error_fixture):
    """Test missing resource api response."""
    fake_resp = mocker.Mock()
    fake_resp.status_code = 404
    fake_resp.json = mocker.Mock(return_value=error_fixture)
    mocker.patch("requests.delete", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    with pytest.raises(Exception) as e_info:
        result = cloudcraft.delete_aws_account("awfda35c-82fe-4edf-b9e9-ffd48f041c22")
    assert str(e_info.value).startswith("Resource not found.")


def test_outdated_resource_response(mocker, error_fixture):
    """Test outdated resource api response."""
    fake_resp = mocker.Mock()
    fake_resp.status_code = 412
    fake_resp.json = mocker.Mock(return_value=error_fixture)
    mocker.patch("requests.put", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    blueprint_data = {}
    with pytest.raises(Exception) as e_info:
        result = cloudcraft.update_blueprint(
            "awfda35c-82fe-4edf-b9e9-ffd48f041c22", blueprint_data
        )
    assert str(e_info.value).startswith("Resource out of date.")


def test_rate_limiting_response(mocker, error_fixture):
    """Test outdated resource api response."""
    fake_resp = mocker.Mock()
    fake_resp.status_code = 429
    fake_resp.json = mocker.Mock(return_value=error_fixture)
    mocker.patch("requests.put", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    blueprint_data = {}
    with pytest.raises(Exception) as e_info:
        result = cloudcraft.update_blueprint(
            "awfda35c-82fe-4edf-b9e9-ffd48f041c22", blueprint_data
        )
    assert str(e_info.value).startswith("Too many requests.")
