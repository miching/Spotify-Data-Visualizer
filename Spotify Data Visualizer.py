#import matplotlib
import json
from collections import Counter


f = open('StreamingHistory0.json')
data = json.load(f)
songHistory = set()

#Get each music stream
for song in data:
    #print(song['trackName'])
    songHistory.add(song['trackName'])
    
print (songHistory)
print ('Total unique songs listened to: ', len(songHistory))

