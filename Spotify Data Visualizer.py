#import matplotlib as plt
from ctypes import alignment
from distutils import sysconfig
from re import T
from xmlrpc.client import boolean
from matplotlib import ticker
import matplotlib.pyplot as plt
import json
from collections import Counter

#songHistory is a dictonary of song(key)-timesPlayed(value)
def readSongHistory(songHistory):

    readAllFiles = True
    amountOfFiles = 0

    while (readAllFiles):
        try:
            fileName = ('StreamingHistory' + str(amountOfFiles) + '.json')
            amountOfFiles = amountOfFiles + 1
            #print (fileName)
            f = open(fileName)
            data = json.load(f)
        #Cannot read file
        except:
            readAllFiles = False
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



#Sort songHistory dict by most played
def sortByMostPlayed(songHistory):
    sortSongHistory = {}
    sortByMostPlayed = sorted(songHistory, key=songHistory.get, reverse=True) 

    for w in sortByMostPlayed:
        sortSongHistory[w] = songHistory[w]

    print (sortSongHistory)

    return sortSongHistory


#Plot all songs
def allSongsListened(songHistory):

    sortSongHistory = sortByMostPlayed(songHistory)
    plt.figure()

    #For each song ever played
    for song in sortSongHistory:
        print(song)
        plt.bar(song, sortSongHistory.get(song) )

    plt.show()



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

        plt.title("Top " + str(number) + " songs listened to")
        plt.xlabel("Song(s)")
        plt.ylabel("Times played")
        #plt.xaxis.set_major_formatter(ticker.NullFormatter())
        plt.xticks([])

    #Display bar graph
    plt.show()

def menu():
    print("1) Top X songs listened to")
    print("2) Top songs listened to by an artist")
    print("3) Listening activity by month")
    print("4) Exit.")


def main():
    print("hello world")
    songHistory = dict()

    #Read all songs from files
    readSongHistory(songHistory)

    #print (songHistory)
    print ('Total unique songs listened to: ', len(songHistory))

    #menu()
    userChoice = int(input(menu()))

    while(userChoice != 4):
        #print("entered here")

        #Print top X songs
        if(userChoice == 1):
            topXSongs = int(input("Range of top songs?") )
            topSongsListened(songHistory, topXSongs)

        if(userChoice == 4):
            break

        else:
            print("Invalid input, Try again.")

        userChoice = input(menu())


    print("Program ended.")

     
main()