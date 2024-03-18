import pytest

from cloudcraftco.cloudcraft import Cloudcraft


@pytest.fixture()
def list_aws_accounts_fixture():
    fixture = {
        "accounts": [
            {
                "id": "awfda35c-82fe-4edf-b9e9-ffd48f041c22",
                "name": "Development",
                "roleArn": "arn:aws:iam::1234567890:role/cloudcraft",
                "externalId": "ex53e827-a724-4a2a-9fec-b13761540785",
                "createdAt": "2022-01-01T21:18:59.057Z",
                "updatedAt": "2022-01-01T21:19:03.487Z",
                "CreatorId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
            }
        ]
    }
    return fixture


def test_list_aws_accounts(mocker, list_aws_accounts_fixture):
    """Test list_aws_accounts handler."""
    fake_resp = mocker.Mock()
    fake_resp.json = mocker.Mock(return_value=list_aws_accounts_fixture)
    fake_resp.status_code = 200
    mocker.patch("requests.get", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    accounts = cloudcraft.list_aws_accounts()

    assert accounts == fake_resp.json()


@pytest.fixture()
def create_aws_account_fixture():
    fixture = {
        "id": "awfda35c-82fe-4edf-b9e9-ffd48f041c22",
        "name": "AWS account name (for example prod or staging)",
        "roleArn": "arn:aws:iam::1234567890:role/cloudcraft",
        "externalId": "ex53e827-a724-4a2a-9fec-b13761540785",
        "CreatorId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
        "updatedAt": "2022-01-01T01:37:55.709Z",
        "createdAt": "2022-01-01T01:37:55.709Z",
    }
    return fixture


def test_create_aws_account(mocker, create_aws_account_fixture):
    """Test create_aws_account handler."""
    fake_resp = mocker.Mock()
    fake_resp.json = mocker.Mock(return_value=create_aws_account_fixture)
    fake_resp.status_code = 201
    mocker.patch("requests.post", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    account = cloudcraft.create_aws_account({"ignore": "me"})

    assert account == fake_resp.json()


@pytest.fixture()
def update_aws_account_fixture():
    fixture = {
        "id": "awfda35c-82fe-4edf-b9e9-ffd48f041c22",
        "name": "Updated AWS account name",
        "roleArn": "arn:aws:iam::1234567890:role/cloudcraft",
        "externalId": "ex53e827-a724-4a2a-9fec-b13761540785",
        "CreatorId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
        "updatedAt": "2022-01-01T01:37:55.709Z",
        "createdAt": "2022-01-01T01:37:55.709Z",
    }
    return fixture


def test_update_aws_account(mocker, update_aws_account_fixture):
    """Test update_aws_account handler."""
    fake_resp = mocker.Mock()
    fake_resp.json = mocker.Mock(return_value=update_aws_account_fixture)
    fake_resp.status_code = 200
    mocker.patch("requests.put", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    account = cloudcraft.update_aws_account("resource-id", {"ignore": "me"})

    assert account == fake_resp.json()


def test_delete_aws_account(mocker):
    """Test delete_aws_account handler."""
    fake_resp = mocker.Mock()
    fake_resp.status_code = 204
    mocker.patch("requests.delete", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    result = cloudcraft.delete_aws_account("resource-id")

    assert result == None


@pytest.fixture()
def read_aws_role_parameters_fixture():
    fixture = {
        "accountId": "1234567890",
        "externalId": "ex53e827-a724-4a2a-9fec-b13761540785",
        "awsConsoleUrl": "https://console.aws.amazon.com/iam/home?#/roles...",
    }
    return fixture


def test_read_aws_role_parameters(mocker, read_aws_role_parameters_fixture):
    """Test read_aws_role_parameters handler."""
    fake_resp = mocker.Mock()
    fake_resp.json = mocker.Mock(return_value=read_aws_role_parameters_fixture)
    fake_resp.status_code = 200
    mocker.patch("requests.get", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    parameters = cloudcraft.read_aws_role_parameters()

    assert parameters == fake_resp.json()


@pytest.fixture()
def snapshot_aws_account_fixture():
    fixture = b'{"tags":["AWS","us-west-2","acct"],"data":{"name":"acct us-west-2 2020-09-01T19:06:08.537Z","grid":"infinite","projection":"isometric","liveOptions":{},"shareDocs":false,"surfaces":[],"connectors":[],"nodes":[]}}'
    return fixture


def test_snapshot_aws_account_200(mocker, snapshot_aws_account_fixture):
    """Test snapshot_aws_account handler when task completes."""
    fake_resp = mocker.Mock()
    fake_resp.content = mocker.Mock(return_value=snapshot_aws_account_fixture)
    fake_resp.status_code = 200
    mocker.patch("requests.get", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    result = cloudcraft.snapshot_aws_account(
        "acct-id", "us-west-2", "json", {"grid": True}
    )

    assert result == fake_resp.content


def test_snapshot_aws_account_202(mocker):
    """Test snapshot_aws_account handler when task times out."""
    fake_resp = mocker.Mock()
    fake_resp.status_code = 202
    mocker.patch("requests.get", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    result = cloudcraft.snapshot_aws_account("id", "us-west-1", "json")

    assert result == {"snapshot_status": "processing"}


@pytest.fixture()
def list_azure_accounts_fixture():
    # hint is substring of clientSecret
    fixture = {
        "accounts": [
            {
                "id": "awfda35c-82fe-4edf-b9e9-ffd48f041c22",
                "name": "Development",
                "applicationId": "dc7e4902-42d1-41c4-be24-f6d07053be95",
                "directoryId": "fb2c1e00-8d07-4fcc-a3c2-74bcda94c520",
                "subscriptionId": "ex53e827-a724-4a2a-9fec-b13761540785",
                "readAccess": [],
                "writeAccess": [],
                "createdAt": "2022-01-01T21:18:59.057Z",
                "updatedAt": "2022-01-01T21:19:03.487Z",
                "CreatorId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
                "hint": "448",
                "source": "azure",
            }
        ]
    }
    return fixture


def test_list_azure_accounts(mocker, list_azure_accounts_fixture):
    """Test list_azure_accounts handler."""
    fake_resp = mocker.Mock()
    fake_resp.json = mocker.Mock(return_value=list_azure_accounts_fixture)
    fake_resp.status_code = 200
    mocker.patch("requests.get", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    accounts = cloudcraft.list_azure_accounts()

    assert accounts == fake_resp.json()


@pytest.fixture()
def create_azure_account_fixture():
    fixture = {
        "id": "awfda35c-82fe-4edf-b9e9-ffd48f041c22",
        "name": "Azure Account",
        "applicationId": "dc7e4902-42d1-41c4-be24-f6d07053be95",
        "directoryId": "fb2c1e00-8d07-4fcc-a3c2-74bcda94c520",
        "subscriptionId": "ex53e827-a724-4a2a-9fec-b13761540785",
        "readAccess": [],
        "writeAccess": [],
        "createdAt": "2022-01-01T21:18:59.057Z",
        "updatedAt": "2022-01-01T21:19:03.487Z",
        "CreatorId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
        "hint": "448",
        "source": "azure",
    }
    return fixture


def test_create_azure_account(mocker, create_azure_account_fixture):
    """Test create_aws_account handler."""
    fake_resp = mocker.Mock()
    fake_resp.json = mocker.Mock(return_value=create_azure_account_fixture)
    fake_resp.status_code = 201
    mocker.patch("requests.post", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    account = cloudcraft.create_azure_account({"ignore": "me"})

    assert account == fake_resp.json()


@pytest.fixture()
def update_azure_account_fixture():
    fixture = {
        "id": "awfda35c-82fe-4edf-b9e9-ffd48f041c22",
        "name": "Updated Azure Account",
        "applicationId": "dc7e4902-42d1-41c4-be24-f6d07053be95",
        "directoryId": "fb2c1e00-8d07-4fcc-a3c2-74bcda94c520",
        "subscriptionId": "ex53e827-a724-4a2a-9fec-b13761540785",
        "readAccess": [],
        "writeAccess": [],
        "createdAt": "2022-01-01T21:18:59.057Z",
        "updatedAt": "2022-01-01T21:19:03.487Z",
        "CreatorId": "us46e9aa-5806-4cd6-8e78-c22d58602d09",
        "hint": "448",
        "source": "azure",
    }
    return fixture


def test_update_azure_account(mocker, update_azure_account_fixture):
    """Test update_azure_account handler."""
    fake_resp = mocker.Mock()
    fake_resp.json = mocker.Mock(return_value=update_azure_account_fixture)
    fake_resp.status_code = 200
    mocker.patch("requests.put", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    account = cloudcraft.update_azure_account("resource-id", {"ignore": "me"})

    assert account == fake_resp.json()


def test_delete_azure_account(mocker):
    """Test delete_azure_account handler."""
    fake_resp = mocker.Mock()
    fake_resp.status_code = 204
    mocker.patch("requests.delete", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    result = cloudcraft.delete_azure_account("resource-id")

    assert result == None


@pytest.fixture()
def snapshot_azure_account_fixture():
    fixture = b'{"tags":["Azure","eastus","acct"],"data":{"name":"acct eastus 2020-09-01T19:06:08.537Z","grid":"infinite","projection":"isometric","liveOptions":{},"shareDocs":false,"surfaces":[],"connectors":[],"nodes":[]}}'
    return fixture


def test_snapshot_azure_account_200(mocker, snapshot_azure_account_fixture):
    """Test snapshot_azure_account handler when task completes."""
    fake_resp = mocker.Mock()
    fake_resp.content = mocker.Mock(return_value=snapshot_azure_account_fixture)
    fake_resp.status_code = 200
    mocker.patch("requests.get", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    result = cloudcraft.snapshot_azure_account(
        "acct-id", "eastus", "json", {"grid": True}
    )

    assert result == fake_resp.content


def test_snapshot_azure_account_202(mocker):
    """Test snapshot_azure_account handler when task times out."""
    fake_resp = mocker.Mock()
    fake_resp.status_code = 202
    mocker.patch("requests.get", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    result = cloudcraft.snapshot_azure_account("id", "eastus", "json")

    assert result == {"snapshot_status": "processing"}
