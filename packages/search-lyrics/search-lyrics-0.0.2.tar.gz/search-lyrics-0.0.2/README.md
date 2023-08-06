# search-lyrics

## Install

```bash
pip install search-lyrics
```

## Usage

### from cmd-line

1. help
```console
$ search-lyrics --help
usage: Search for song containing lyrics [-h] [--artist artist] [--text text] [--genius-access-token genius_access_token] [--verbose]
                                         [--version]

options:
  -h, --help            show this help message and exit
  --artist artist       Artist to search text into
  --text text           text to search
  --genius-access-token genius_access_token
                        access token to use for genius api (by default, search for GENIUS_ACCESS_TOKEN in ENV variables)
  --verbose             Enable verbose output
  --version             Show version and exit
```

2. search Neoni song containing "heaven can't help me now"
```console
$ search-lyrics --artist "Neoni" --text "heaven can't help me now" --genius-access-token "PUT HERE YOUR GENIUS ACCESS TOKEN"
SANCTUARY
```

### from python

```python
from search_lyrics import search_lyrics
songs = search_lyrics("Neoni", "heaven can't help me now", "PUT HERE YOUR GENIUS ACCESS TOKEN")
for song in songs:
    print(song.title)
```
