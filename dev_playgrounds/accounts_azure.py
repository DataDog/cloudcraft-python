import os

from cloudcraftco.cloudcraft import Cloudcraft

# Azure Account record crud operations...
#
# running playground...
# % cd {repo_directory}
# % poetry shell
# % poetry install
# % export CLOUDCRAFT_API_KEY={{ api-key }}
# % export CLOUDCRAFT_TEST_SUBSCRIPTION={{ your-subscription-id }}
# % export CLOUDCRAFT_TEST_DIRECTORY={{ your-directory-id }}
# % export CLOUDCRAFT_TEST_APPLICATION={{ your-application-id }}
# % export CLOUDCRAFT_TEST_SECRET={{ your-client-secret }}
# % python3 dev_playgrounds/accounts_azure.py

cloudcraft = Cloudcraft({"host": "localhost", "port": 3000, "protocol": "http"})
subscription = os.environ.get("CLOUDCRAFT_TEST_SUBSCRIPTION")
directory = os.environ.get("CLOUDCRAFT_TEST_DIRECTORY")
application = os.environ.get("CLOUDCRAFT_TEST_APPLICATION")
secret = os.environ.get("CLOUDCRAFT_TEST_SECRET")

# list azure accounts
accounts = cloudcraft.list_azure_accounts()
print("original-azure-accounts ::\n" + str(accounts))
print("******************************************\n")


# create azure account
# id and secret values must be valid
data = {
    "name": "Playground Azure Account",
    "subscriptionId": subscription,
    "directoryId": directory,
    "applicationId": application,
    "clientSecret": secret,
}
result = cloudcraft.create_azure_account(data)
print("post-post-account ::\n" + str(result))
print("******************************************\n")

test_account_id = result["id"]
print("test-account-id :: " + test_account_id)
print("******************************************\n")


# update azure account
data = {
    "name": "Updated Playground Azure Account",
    "subscriptionId": subscription,
    "directoryId": directory,
    "applicationId": application,
}
result = cloudcraft.update_azure_account(test_account_id, data)
print("put-azure-account ::\n" + str(result))
print("******************************************\n")


# delete azure account
result = cloudcraft.delete_azure_account(test_account_id)
print("delete-azure-account ::\n" + str(result))
print("******************************************\n")


# list azure accounts
accounts = cloudcraft.list_azure_accounts()
print("modified-azure-accounts ::\n" + str(accounts))
print("******************************************\n")
