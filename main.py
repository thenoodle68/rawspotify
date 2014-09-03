# Create Artist - Track list from Spotify playlist

import json
import urllib

# Copy songs from Spotify client and paste below
raw = """
http://open.spotify.com/track/67awxiNHNyjMXhVgsHuIrs
""".split("\n")
ids = []

# Grab IDs from paste
for x in raw:
    if x and "/local/" not in x:
        ids.append(x.replace("http://open.spotify.com/track/", ""))

# Maintain chronological order when adding
ids.reverse()

# Use Spotify API to receive data
for x in ids:
    durl = urllib.urlopen("https://api.spotify.com/v1/tracks/" + x)
    data = json.loads(durl.read())
    print "{} - {}".format(data["artists"][0]["name"],data["name"])
