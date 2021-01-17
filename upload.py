import json
import os
from mutagen.mp3 import MP3

data = json.load(open('data.json','r'))

for filenames in os.walk('songs'):
    for song in filenames[2]:
        time = MP3('songs/'+song).info.length
        data["songs"].append({
            "link" :  "https://saranmahadev.tech/music/songs/"+song,
            "song" : song.split('.')[0],
            "time" : str(round(time/60,2)),
            "image": "https://saranmahadev.tech/music/image.jpg"
        })      

with open('data.json','w') as outfile:
    json.dump(data,outfile)
        
     
