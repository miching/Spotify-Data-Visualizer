#import matplotlib as plt
import matplotlib.pyplot as plt
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

plt.figure()

#For each unique song
for song in uniqueSongs:
    count = 0

    #For each song ever played
    for countSong in songHistory:
        if(song == countSong):
            count = count + 1

    print('Song Title: ', song, ' Played: ', count)

    plt.bar(song, count)

plt.show()