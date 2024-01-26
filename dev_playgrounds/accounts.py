import os

from cloudcraftco.cloudcraft import Cloudcraft

# AWS Account record crud operations...
#
# running playground...
# % cd {repo_directory}
# % poetry shell
# % poetry install
# % export CLOUDCRAFT_TEST_ROLE={{ your-test-role-arn }}
# % python3 dev_playgrounds/accounts.py

cloudcraft = Cloudcraft({"host": "localhost", "port": 3000, "protocol": "http"})
role = os.environ.get("CLOUDCRAFT_TEST_ROLE")

# read aws role paramaters
params = cloudcraft.read_aws_role_parameters()
print("iam-params ::\n" + str(params))
print("******************************************\n")


# list aws accounts
accounts = cloudcraft.list_aws_accounts()
print("original-accounts ::\n" + str(accounts))
print("******************************************\n")


# create aws account
# role must exist and match your api_key/account
data = {"name": "Playground AWS Account", "roleArn": role}
result = cloudcraft.create_aws_account(data)
print("post-account ::\n" + str(result))
print("******************************************\n")

test_account_id = result["id"]
print("test-account-id :: " + test_account_id)
print("******************************************\n")


# update aws account
data = {"name": "Updated Playground AWS Account.", "roleArn": role}
result = cloudcraft.update_aws_account(test_account_id, data)
print("put-account ::\n" + str(result))
print("******************************************\n")


# delete aws account
result = cloudcraft.delete_aws_account(test_account_id)
print("delete-account ::\n" + str(result))
print("******************************************\n")


# list aws accounts
accounts = cloudcraft.list_aws_accounts()
print("modified-accounts ::\n" + str(accounts))
print("******************************************\n")
