import json
import eyed3
import os

data = json.load(open('data.json','r'))

for filenames in os.walk('songs'):
    for song in filenames[2]:
        print("link:"+"https://saranmahadev.tech/songs/"+song)
        
        # sdata = data["songs"].append({
            # "song" : audio_file.tag.album
        # })      
# 
        # print(sdata)
        
     
