def _send_request(res):
    json = res.json()
    if res.status_code != 200 or not json.get('success', True):
        raise Exception(json.get("error_code", "Oops! An error occurred."))
    return json