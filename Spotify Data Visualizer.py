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


        #Print all music streams
        #for song in data:

        #    print (song)
        

        return data
            


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

    songTimesPlayed = {}

    #Print all music streams
    for song in songHistory:

        #print ("myloop", song['trackName'])
        print ("myloop",song)

        #print(song.keys())
        songTitle = song.get("trackName")

        #If song already added to songTimesPlayed Dictionary, update times played
        if(songTitle in songTimesPlayed):
            timesPlayed = songTimesPlayed[songTitle]
            timesPlayed = timesPlayed + 1
            songTimesPlayed[songTitle] = timesPlayed
            

        #Song doesn't exist in songTimesPlayed dictionary, initialize
        else:
            songTimesPlayed[songTitle] = 1
        

    songTimesPlayed = sorted(songTimesPlayed, key=songTimesPlayed.get, reverse=True) 

    return songTimesPlayed


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

    #Display bar graph
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