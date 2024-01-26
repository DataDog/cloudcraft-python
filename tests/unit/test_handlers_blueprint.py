import pytest

from cloudcraftco.cloudcraft import Cloudcraft


@pytest.fixture()
def list_blueprints_fixture():
    fixture = {
        "blueprints": [
            {
                "id": "bp37712a-c507-4c62-ad8b-7d981cacb3be",
                "name": "Web App Reference Architecture",
                "createdAt": "2022-01-01T20:54:47.302Z",
                "updatedAt": "2022-01-01T20:55:52.876Z",
                "CreatorId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
                "LastUserId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
            }
        ]
    }
    return fixture


def test_list_blueprints(mocker, list_blueprints_fixture):
    """Test list_blueprints handler."""
    fake_resp = mocker.Mock()
    fake_resp.json = mocker.Mock(return_value=list_blueprints_fixture)
    fake_resp.status_code = 200
    mocker.patch("requests.get", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    blueprints = cloudcraft.list_blueprints()

    assert blueprints == fake_resp.json()


@pytest.fixture()
def create_blueprint_fixture():
    fixture = {
        "id": "bp37712a-c507-4c62-ad8b-7d981cacb3be",
        "LastUserId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
        "CreatorId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
        "data": {"grid": "standard", "name": "My new blueprint", "version": 1},
        "updatedAt": "2022-01-01T20:59:57.340Z",
        "createdAt": "2022-01-01T20:59:57.340Z",
    }
    return fixture


def test_create_blueprint(mocker, create_blueprint_fixture):
    """Test create_blueprint handler."""
    fake_resp = mocker.Mock()
    fake_resp.json = mocker.Mock(return_value=create_blueprint_fixture)
    fake_resp.status_code = 201
    mocker.patch("requests.post", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    blueprint = cloudcraft.create_blueprint({"ignore": "me"})

    assert blueprint == fake_resp.json()


@pytest.fixture()
def read_blueprint_fixture():
    fixture = {
        "id": "bp37712a-c507-4c62-ad8b-7d981cacb3be",
        "data": {"note": "See Blueprint data format specification"},
        "createdAt": "2022-01-01T20:54:47.302Z",
        "updatedAt": "2022-01-01T20:55:52.876Z",
        "CreatorId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
        "LastUserId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
    }
    return fixture


def test_read_blueprint(mocker, read_blueprint_fixture):
    """Test read_blueprint handler."""
    fake_resp = mocker.Mock()
    fake_resp.json = mocker.Mock(return_value=read_blueprint_fixture)
    fake_resp.status_code = 200
    mocker.patch("requests.get", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    blueprint = cloudcraft.read_blueprint("awfda35c-82fe-4edf-b9e9-ffd48f041c22")

    assert blueprint == fake_resp.json()


def test_update_blueprint(mocker):
    """Test update_blueprint handler."""
    fake_resp = mocker.Mock()
    fake_resp.status_code = 204
    mocker.patch("requests.put", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    account = cloudcraft.update_blueprint("resource-id", {"ignore": "me"})

    assert account == None


def test_delete_blueprint(mocker):
    """Test delete_blueprint handler."""
    fake_resp = mocker.Mock()
    fake_resp.status_code = 204
    mocker.patch("requests.delete", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    result = cloudcraft.delete_blueprint("resource-id")

    assert result == None


@pytest.fixture()
def export_blueprint_fixture():
    fixture = b'<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"\n  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="ccdiagram"></svg>'
    return fixture


def test_export_blueprint(mocker, export_blueprint_fixture):
    """Test export_blueprint handler when task completes."""
    fake_resp = mocker.Mock()
    fake_resp.content = mocker.Mock(return_value=export_blueprint_fixture)
    fake_resp.status_code = 200
    mocker.patch("requests.get", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    result = cloudcraft.export_blueprint(
        "awfda35c-82fe-4edf-b9e9-ffd48f041c22", "svg", {"grid": True}
    )

    assert result == fake_resp.content
