import requests

from galiboo import API_HOST
from ..utils import _send_request


def search_tracks(track=None, artist=None, limit=10, page=1):
    from galiboo.auth import auth_token

    if (track and artist) or (not track and not artist):
        raise Exception("Please provide exactly one of the following: 'artist' and 'track'.")

    params = {"token" : auth_token, 'limit' : limit, 'page' : page}

    if track:
        params['track'] = track
    else:
        params['artist'] = artist

    return _send_request(
        requests.get(API_HOST + "/metadata/tracks/search/", params=params)
    )