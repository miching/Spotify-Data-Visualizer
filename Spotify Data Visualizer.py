#import matplotlib as plt
from distutils import sysconfig
from re import T
import matplotlib.pyplot as plt
import json
from collections import Counter

#songHistory is a dictonary of song(key)-timesPlayed(value), amountOfFile is user input int
def readSongHistory(songHistory, amountOfFiles):

    #Read X number of files
    for i in range(amountOfFiles):
        try:
            fileName = ('StreamingHistory' + str(i) + '.json')
            #print (fileName)
            f = open(fileName)
            data = json.load(f)
        except:
            print("Cannot read file")

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



def main():
     print("hello world")
     songHistory = dict()

     numOfFiles = int(input("How many files to read?") )

    #Read all songs from files
     readSongHistory(songHistory, numOfFiles)

     #print (songHistory)
     print ('Total unique songs listened to: ', len(songHistory))

     topXSongs = int(input("Range of top songs?") )
     topSongsListened(songHistory, topXSongs)



#Sort songHistory dict by most played
def sortByMostPlayed(songHistory):
    sortSongHistory = {}
    sortByMostPlayed = sorted(songHistory, key=songHistory.get, reverse=True) 

    for w in sortByMostPlayed:
        sortSongHistory[w] = songHistory[w]

    print (sortSongHistory)

    return sortSongHistory


def allSongsListened():
    print()
    #For each song ever played
    #for song in sortSongHistory:
        #print(song)
    #   plt.bar(song, sortSongHistory.get(song) )



#Plot the top 'number' of songs listened to
#songHistory is dict of all songs, number is user input of desired X top songs
def topSongsListened(songHistory, number):
    sortSongHistory = sortByMostPlayed(songHistory)

    plt.figure()

    #Top number most listened songs, using iterator
    it = iter(sortSongHistory)
    for song in range(number):

        #Get song title
        songTitle = next(it)

        #X-cords is song title, Y-cords is the value/number of times played
        plt.bar(songTitle, sortSongHistory.get(songTitle) )

        #Show number of times played on graph
        plt.text(song, sortSongHistory.get(songTitle), sortSongHistory.get(songTitle) ,color = 'blue', fontweight = 'bold')

        #Iterate to next song
        next(it)

    plt.show()



def main():
     print("hello world")
     songHistory = dict()

     numOfFiles = int(input("How many files to read?") )

    #Read all songs from files
     readSongHistory(songHistory, numOfFiles)

     #print (songHistory)
     print ('Total unique songs listened to: ', len(songHistory))

     topXSongs = int(input("Range of top songs?") )
     topSongsListened(songHistory, topXSongs)

main()