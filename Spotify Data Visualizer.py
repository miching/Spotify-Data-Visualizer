import matplotlib as plt
import json
from collections import Counter


f = open('StreamingHistory0.json')
data = json.load(f)
songHistory = list()

#Get each music stream
for song in data:
    #print(song['trackName'])
    songHistory.append(song['trackName'])

uniqueSongs = set(songHistory)
print (songHistory)
print ('Total songs listened to: ', len(songHistory))
print ('Total unique songs listened to: ', len(uniqueSongs))

