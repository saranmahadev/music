import json
import os
from mutagen.mp3 import MP3

data = json.load(open('data.json','r'))

for filenames in os.walk('songs'):
    for song in filenames[2]:
        time = MP3('songs/'+song).info.length
        songdict = {
            "link" :  "http://saranmahadev.tech/music/songs/"+song,
            "song" : song.split('.')[0],
            "time" : str(round(time/60,2))
        }
        if songdict not in data["songs"]:
            data["songs"].append(songdict)      

with open('data.json','w') as outfile:
    json.dump(data,outfile)
        
     
