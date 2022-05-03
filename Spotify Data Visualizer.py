#import matplotlib as plt
from distutils import sysconfig
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

    
#print (songHistory)
print ('Total unique songs listened to: ', len(songHistory))

plt.figure()

sortSongHistory = {}
sortByMostPlayed = sorted(songHistory, key=songHistory.get, reverse=True) 

for w in sortByMostPlayed:
    sortSongHistory[w] = songHistory[w]

print (sortSongHistory)

#For each song ever played
#for song in sortSongHistory:
    #print(song)
 #   plt.bar(song, sortSongHistory.get(song) )

it = iter(sortSongHistory)
for song in range(10):
    songTitle = next(it)
    plt.bar(songTitle, sortSongHistory.get(songTitle) )
    next(it)

plt.show()