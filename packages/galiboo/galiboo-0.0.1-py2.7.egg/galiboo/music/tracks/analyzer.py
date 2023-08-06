import requests

from galiboo import API_HOST
from ..utils import _send_request


def analyze_music_from_url(url):
    from galiboo.auth import auth_token
    return _send_request( requests.get(API_HOST + "/analyzer/analyze_url/", params={"token" : auth_token, "url" : url}) )

# def analyze_music_from_file(file_):
#     from auth import auth_token
#
#     assert isinstance(file_, file)
#     files = {'file': file_}
#
#     return _send_request(requests.get(API_HOST + "/analyzer/analyze_file/", params={"token": auth_token}, files=files))

def analyze_music_from_youtube(youtube_url):
    from galiboo.auth import auth_token
    return _send_request( requests.get(API_HOST + "/analyzer/analyze_youtube/", params={"token" : auth_token, "url" : youtube_url}) )
