api_key = "<your api key goes here>"

from galiboo import auth, music

auth.set_api_key(api_key)

print music.find_tracks_by_text_query("piano")

print music.get_track("5a419ed78cc3d0d2d4249ebb") # Charlie Puth's "Attention"
print music.search_tracks("Attention")
print music.search_tracks(artist="Camila Cabello")
print music.get_artist("5a43dfbec3de0d102316497e") # Charlie Puth

print music.search_artists("Charlie Puth")
print music.find_similar_tracks("5a419ed78cc3d0d2d4249ebb")