# A configuration file for Spotted on Spotify

VERSION='1.0.0'

YOUTUBE_DL_OPTS={
  'format' : 'bestaudio',
  'postprocessors' : [{
    'key' : 'FFmpegExtractAudio',
    'preferredcodec' : 'mp3',
    'preferredquality' : '256'
  }],
  'quiet' : True,
  'no_warnings' : True,
  'outtmpl' : '/tmp/download.mp3'
}

SPOTIPY_SCOPE = 'playlist-modify-public'
SPOTIPY_CLIENT_ID='a6a7974f555849a8b63e9191ebc12629'
SPOTIPY_CLIENT_SECRET='c13b81df0c33434ea4596c9589ca1aab'
SPOTIPY_REDIRECT_URI='https://github.com/anthonymirand/SpottedOnSpotify-cmdline'

ACOUSTID_API_KEY='qY3621bc1V'
