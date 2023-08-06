auth_token = None


def set_api_key(api_key):
    global auth_token
    auth_token = api_key