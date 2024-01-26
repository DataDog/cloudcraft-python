import os

from .api_account import (
    create_aws_account_handler,
    delete_aws_account_handler,
    list_aws_accounts_hander,
    read_aws_role_parameters_handler,
    snapshot_aws_account_handler,
    update_aws_account_handler,
)
from .api_blueprint import (
    create_blueprint_handler,
    delete_blueprint_handler,
    export_blueprint_handler,
    list_blueprints_handler,
    read_blueprint_handler,
    update_blueprint_handler,
)
from .api_budget import export_blueprint_budget_handler
from .api_user import read_user_profile_handler
from .error import (
    CloudcraftForbidden,
    CloudcraftMalformed,
    CloudcraftMissingResource,
    CloudcraftOutdatedResource,
    CloudcraftRateLimiting,
    CloudcraftUnauthorized,
    CloudcraftUnexpected,
)


def get_env_config():
    """Obtain config values defined via environment variables."""
    config_via_env = {}
    max_network_retries = os.environ.get("CLOUDCRAFT_MAX_NETWORK_RETRIES")
    if max_network_retries:
        config_via_env["max_network_retries"] = int(max_network_retries)
    timeout = os.environ.get("CLOUDCRAFT_TIMEOUT")
    if timeout:
        config_via_env["timeout"] = int(timeout)
    host = os.environ.get("CLOUDCRAFT_HOST")
    if host:
        config_via_env["host"] = host
    port = os.environ.get("CLOUDCRAFT_PORT")
    if port:
        config_via_env["port"] = int(port)
    protocol = os.environ.get("CLOUDCRAFT_PROTOCOL")
    if protocol:
        config_via_env["protocol"] = protocol
    api_key = os.environ.get("CLOUDCRAFT_API_KEY")
    if api_key:
        config_via_env["api_key"] = api_key
    return config_via_env


class Cloudcraft:
    """Initialize Cloudcraft API client instance."""

    def __init__(self, config=None):
        if config is None:
            config = {}
        self.config = {}
        # default config
        config_defaults = {
            "max_network_retries": 10,
            "timeout": 80000,
            "host": "api.cloudcraft.co",
            "port": 443,
            "protocol": "https",
        }
        # environment config
        config_via_env = get_env_config()
        # finalize config
        self.config = {**config_defaults, **config_via_env, **config}
        # raise if no api key
        try:
            self.config["api_key"]
        except KeyError:
            raise KeyError(
                "api_key must be set via config or environment variable."
            ) from None
        # create url template
        url_base = "{protocol}://{host}".format(**self.config)
        if self.config.get("port"):
            url_base = url_base + ":" + str(self.config.get("port"))
        if "localhost" in url_base:
            url_base = url_base + "/api"
        self.url_base = url_base + "{}"
        # request headers
        self.headers = {
            "Authorization": "Bearer {}".format(self.config["api_key"]),
            "Content-Type": "application/json",
        }
        # convert timeout
        self.timeout_seconds = 0.001 * self.config["timeout"]

    @staticmethod
    def assemble_message(base, error):
        """Include API error message with exception."""
        message = base
        if error:
            message = message + " [Error: " + error + "]"
        return message

    @staticmethod
    def check_errors(response, documented_errors={401, 429}):
        """Map API response status code to Cloudcraft errors."""
        status_code = response.status_code
        if status_code >= 200 and status_code <= 299:
            return
        else:
            error = response.json().get("error")
        if status_code not in documented_errors:
            # print("unexpected-status :: " + str(status_code))
            details = Cloudcraft.assemble_message(
                "Undocumented Response. Please let us know: <support@cloudcraft.co>.",
                error,
            )
            raise CloudcraftUnexpected(details)
        elif status_code == 400:
            details = Cloudcraft.assemble_message(
                "Malformed request.",
                error,
            )
            raise CloudcraftMalformed(details)
        elif status_code == 401:
            details = Cloudcraft.assemble_message(
                "Unauthorized request.",
                error,
            )
            raise CloudcraftUnauthorized(details)
        elif status_code == 403:
            details = Cloudcraft.assemble_message(
                "Forbidden, insufficient priviledges.",
                error,
            )
            raise CloudcraftForbidden(details)
        elif status_code == 404:
            details = Cloudcraft.assemble_message(
                "Resource not found.",
                error,
            )
            raise CloudcraftMissingResource(details)
        elif status_code == 412:
            details = Cloudcraft.assemble_message(
                "Resource out of date.",
                error,
            )
            raise CloudcraftOutdatedResource(details)
        elif status_code == 429:
            details = Cloudcraft.assemble_message(
                "Too many requests.",
                error,
            )
            raise CloudcraftRateLimiting(details)

    # API - AWS Account
    def list_aws_accounts(self):
        """List AWS accounts via api request."""
        # expected: [200, 401, 429]
        response = list_aws_accounts_hander(self)
        Cloudcraft.check_errors(response)
        return response.json()

    def create_aws_account(self, data):
        """Create AWS account via api request."""
        # expected: [201, 401, 403, 429]
        response = create_aws_account_handler(self, data)
        Cloudcraft.check_errors(response, {401, 403, 429})
        return response.json()

    def update_aws_account(self, account_id, data):
        """Update AWS account via api request."""
        # expected: [200, 401, 403, 404, 429]
        response = update_aws_account_handler(self, account_id, data)
        Cloudcraft.check_errors(response, {400, 401, 403, 404, 429})
        return response.json()

    def delete_aws_account(self, account_id):
        """Delete AWS account via api request."""
        # expected: [204, 401, 403, 404, 429]
        response = delete_aws_account_handler(self, account_id)
        Cloudcraft.check_errors(response, {400, 401, 403, 404, 429})
        return

    def read_aws_role_parameters(self):
        """Read AWS role parameters via api request."""
        # expected: [200, 401, 429]
        response = read_aws_role_parameters_handler(self)
        Cloudcraft.check_errors(response)
        return response.json()

    def snapshot_aws_account(self, account_id, region, ss_format, options=None):
        """Export AWS account snapshot via api request."""
        # expected: [200, 202, 401, 403, 404, 429]
        response = snapshot_aws_account_handler(
            self, account_id, region, ss_format, options
        )
        Cloudcraft.check_errors(response, {400, 401, 403, 404, 429})
        if response.status_code == 202:
            return {"snapshot_status": "processing"}
        else:
            return response.content

    # API - BLUEPRINT
    def list_blueprints(self):
        """List blueprints via api request."""
        # expected: [200, 401, 429]
        response = list_blueprints_handler(self)
        Cloudcraft.check_errors(response)
        return response.json()

    def create_blueprint(self, data):
        """Create blueprint via api request."""
        # expected: [200, 401, 403, 429]
        response = create_blueprint_handler(self, data)
        Cloudcraft.check_errors(response, {401, 403, 429})
        return response.json()

    def read_blueprint(self, blueprint_id):
        """Read blueprint via api request."""
        # expected: [200, 401, 403, 404, 429]
        response = read_blueprint_handler(self, blueprint_id)
        Cloudcraft.check_errors(response, {400, 401, 403, 404, 429})
        return response.json()

    def update_blueprint(self, blueprint_id, data):
        """Update blueprint via api request."""
        # expected: [204, 401, 403, 404, 412, 429]
        response = update_blueprint_handler(self, blueprint_id, data)
        Cloudcraft.check_errors(response, {400, 401, 403, 404, 412, 429})
        return

    def delete_blueprint(self, blueprint_id):
        """Delete blueprint via api request."""
        # expected: [204, 401, 403, 404, 429]
        response = delete_blueprint_handler(self, blueprint_id)
        Cloudcraft.check_errors(response, {400, 401, 403, 404, 429})
        return

    def export_blueprint(self, bp_id, bp_format, options=None):
        """Export blueprint via api request."""
        # expected: [200, 401, 403, 404, 429]
        response = export_blueprint_handler(self, bp_id, bp_format, options)
        Cloudcraft.check_errors(response, {400, 401, 403, 404, 429})
        return response.content

    # API - BUDGET
    def export_blueprint_budget(self, bp_id, bp_format, options=None):
        """Export blueprint budget via api request."""
        # expected: [200, 401, 403, 404, 429]
        response = export_blueprint_budget_handler(self, bp_id, bp_format, options)
        Cloudcraft.check_errors(response, {400, 401, 403, 404, 429})
        return response.content

    # API - USER
    def read_user_profile(self):
        """Read Cloudcraft app user properties via api request."""
        # expected: [200, 401, 429]
        response = read_user_profile_handler(self)
        Cloudcraft.check_errors(response)
        return response.json()
