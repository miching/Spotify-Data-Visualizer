#import matplotlib as plt
from re import T
import matplotlib.pyplot as plt
import json
from collections import Counter


f = open('StreamingHistory0.json')
data = json.load(f)
songHistory = dict()

#Get each music stream
for song in data:

    #If song already added to songHistory Dictionary, update times played
    if(song['trackName'] in songHistory):
        timesPlayed = songHistory[song['trackName']]
        timesPlayed = timesPlayed + 1
        songHistory[song['trackName']] = timesPlayed

    #Song doesn't exist in songHistory dictionary, initialize
    else:
        songHistory[song['trackName']] = 1

    
print (songHistory)
print ('Total unique songs listened to: ', len(songHistory))

plt.figure()

sortListenHistory = {}
sortByMostPlayed = sorted(songHistory, key=songHistory.get, reverse=True) 

for w in sortByMostPlayed:
    sortListenHistory[w] = songHistory[w]

print (sortListenHistory)

#For each song ever played
for song in sortListenHistory:
    #print(song)
    plt.bar(song, sortListenHistory.get(song) )

plt.show()