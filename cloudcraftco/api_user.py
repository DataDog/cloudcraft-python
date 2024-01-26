import requests


def read_user_profile_handler(cloudcraft):
    """Request user details via Cloudcraft api."""
    # /user/me
    # method: get
    api_route = "/user/me"
    url = cloudcraft.url_base.format(api_route)
    return requests.get(
        url, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )
