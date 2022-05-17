#import matplotlib as plt
from ctypes import alignment
from distutils import sysconfig
from re import T
from xmlrpc.client import boolean
from matplotlib import ticker
import matplotlib.pyplot as plt
import json
from collections import Counter

#Read all JSON files and transform into dict 
def readSongHistory():

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


        #Print all music streams
        #for song in data:

        #    print (song)
        

        return data
            


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

        plt.title("Top " + str(number) + " songs listened to")
        plt.xlabel("Song(s)")
        plt.ylabel("Times played")
        #plt.xaxis.set_major_formatter(ticker.NullFormatter())
        plt.xticks([])

    #Display bar graph
    plt.show()

#Plot the songs listened to by artist
def songsByArtist(songHistory, artistName):

    it = iter(songHistory)
    for song in songHistory:
        print()
        



def menu():
    print("1) Top X songs listened to")
    print("2) Top songs listened to by an artist")
    print("3) Listening activity by month")
    print("4) Exit.")


def main():
    print("hello world")

    #Read all songs from files
    songHistory = readSongHistory()

    #print (songHistory)
    print ('Total unique songs listened to: ', len(songHistory))

    #menu()
    userChoice = int(input(menu()))

    while(userChoice != 4):
        #print("entered here")

        #Print top X songs
        if(userChoice == 1):
            topXSongs = int(input("Range of top songs?") )
            temp = sortByMostPlayed(songHistory)
            topSongsListened(temp, topXSongs)

        #Print top songs listened by artist
        if(userChoice == 2):
            artistSongs = int(input("Name of artist?") )

        if(userChoice == 4):
            break

        else:
            print("Invalid input, Try again.")

        userChoice = input(menu())


    print("Program ended.")

     
main()