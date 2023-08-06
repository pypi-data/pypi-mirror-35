![Galiboo](./assets/logo.png)

# Python SDK for Galiboo's A.I. Music API (beta)
https://galiboo.com

## API key
Be sure to get an API key from <a href="https://galiboo.com">https://galiboo.com</a> to use this library.

## Installation

```bash
pip install galiboo
```

## Usage
Here are some examples. 
You can also checkout our API docs at: <a href="https://apidocs.galiboo.com">https://apidocs.galiboo.com</a>

### Authentication
Always set your API key first, before calling any other API endpoints.

```python
from galiboo import auth
auth.set_api_key("<your api key>")
```


### AI-powered search for music
Find tracks that are relevant to any natural language query, auto-magically.
```python
from galiboo import auth, music
auth.set_api_key("<your api key>")

# Let's search for some relaxing music
query = "soft, piano tunes"
tracks = music.find_tracks_by_text_query(query)
```

### Get a track's music analysis data
```python
from galiboo import auth, music
auth.set_api_key("<your api key>")

# Let's get the moods, emotions, & other music analysis data
# that Galiboo's Music A.I. has extracted for Coldplay's "Viva la Vida"

viva_la_vida = music.get_track("5a3fc326d836490c18703e3f")

print viva_la_vida['analysis']
print viva_la_vida['analysis']['smart_tags']
# etc...
```

### Find tracks by tags
```python
from galiboo import auth, music
auth.set_api_key("<your api key>")

# Let's find some nice music for doing focus work
query = {
    "energy" : 0.25,
    "smart_tags" : {
         "Emotion-Calming_/_Soothing" : 0.9
    }
    # etc. (see our API docs for more info)
}

tracks = music.find_tracks_by_tags(query)
print tracks
```

### Find similar-sounding tracks
```python
from galiboo import auth, music
auth.set_api_key("<your api key>")

# Let's find similar tracks to Coldplay's Viva la Vida
similar_tracks = music.find_similar_tracks("5a3fc326d836490c18703e3f")

print similar_tracks
```

### Analyze music from a URL
```python
from galiboo import auth, music
auth.set_api_key("<your api key>")

# Let's analyze the audio at this URL
audio_url = "https://storage.googleapis.com/gb_spotify20k/spotify_preview_audios/4iLqG9SeJSnt0cSPICSjxv.mp3"
analysis = music.analyze_music_from_url(audio_url)

print analysis
```

### Analyze music from a YouTube video
```python
from galiboo import auth, music
auth.set_api_key("<your api key>")

# Let's analyze the audio at this URL
youtube_video = "https://www.youtube.com/watch?v=nfs8NYg7yQM"
analysis = music.analyze_music_from_youtube(youtube_video)

print analysis
```

### Schedule a music analysis job
```python
from galiboo import auth, music
auth.set_api_key("<your api key>")

# Let's schedule a job in Galiboo's cloud to analyze the audio at this URL
audio_url = "https://storage.googleapis.com/gb_spotify20k/spotify_preview_audios/4iLqG9SeJSnt0cSPICSjxv.mp3"
job = music.add_analysis_job(audio_url)

print job
```

### View a music analysis job
```python
from galiboo import auth, music
auth.set_api_key("<your api key>")

# Let's get the status/results of an analysis job that we scheduled
job_id = "5b8c17c9011610000bc2de67"
job = music.get_analysis_job(job_id)

print job
```

### View all music analysis jobs
```python
from galiboo import auth, music
auth.set_api_key("<your api key>")

# Let's get the status/results of all the analysis jobs that we scheduled
jobs = music.get_all_analysis_jobs(page=1)
print jobs
```

### Search for tracks
```python
from galiboo import auth, music
auth.set_api_key("<your api key>")

# Let's search for Charlie Puth's Attention
track = "Attention"
tracks = music.search_tracks(track=track)
```

### Search for artists
```python
from galiboo import auth, music
auth.set_api_key("<your api key>")

# Let's search for some relaxing music
artist = "Camila Cabello"
artists = music.search_artists(artist)
```


### Get an artist's metadata
```python
from galiboo import auth, music
auth.set_api_key("<your api key>")

coldplay = music.get_artist("5a3fc2ffd836490c18703c7d")

print coldplay['tracks']
```

## Last words
Be sure to checkout our API docs at <a href="apidocs.galiboo.com">apidocs.galiboo.com</a> and visit our website (<a href="https://galiboo.com">galiboo.com</a>) for more information.

If you have any questions, feel free to email us at <a href="mailto:hello@galiboo.com">hello@galiboo.com</a>, and we'll get back to you ASAP! :)