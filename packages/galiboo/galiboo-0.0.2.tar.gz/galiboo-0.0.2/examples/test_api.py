from galiboo import auth, music

api_key = "<your api key>"

auth.set_api_key(api_key)

print music.find_tracks_by_text_query("piano")

print music.get_track("5a419ed78cc3d0d2d4249ebb") # Charlie Puth's "Attention"
print music.search_tracks("Attention")
print music.search_tracks(artist="Camila Cabello")
print music.get_artist("5a43dfbec3de0d102316497e") # Charlie Puth

print music.search_artists("Charlie Puth")
print music.find_similar_tracks("5a419ed78cc3d0d2d4249ebb") # Tracks similar to Charlie Puth's "Attention"

# Sample query below
query = {
	"energy" : 0.2,
	"smart_tags" : {
		"Emotion-Calming_/_Soothing" : 0.9
	}
	# ... add any other tags/search criteria that you'd like!
}

print music.find_tracks_by_tags(tags_query=query)

print music.analyze_music_from_url("https://storage.googleapis.com/gb_spotify20k/spotify_preview_audios/4iLqG9SeJSnt0cSPICSjxv.mp3")
print music.analyze_music_from_youtube("https://www.youtube.com/watch?v=nfs8NYg7yQM")