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
            


#Plot all songs
def allSongsListened(songHistory):

    sortSongHistory = sortByMostPlayed(songHistory)
    plt.figure()

    #For each song ever played
    for song in sortSongHistory:
        print(song)
        plt.bar(song, sortSongHistory.get(song) )

    plt.show()



#Get top N (number) songs listened to
def topSongsListenedTo(songHistory, number):

    songTimesPlayed = {}
    listOfSongTitles = [song['trackName'] for song in songHistory]
    print ("vals: ", listOfSongTitles)

    uniqueSongTitles = set(listOfSongTitles)

    for songTitles in uniqueSongTitles:
        songTimesPlayed[songTitles] =  0

    print("Total Unique songs: ",len(uniqueSongTitles))


    #For each unique song title
    for uniqueSong in uniqueSongTitles:

        #For all songs listened to
        for song in songHistory:
            songTitle = song["trackName"]
           
           #Song has been listened to
            if(songTitle == uniqueSong):
                songTimesPlayed[songTitle] = songTimesPlayed[songTitle] + 1

    print(songTimesPlayed)

    topNSongsList = [{'',0}] * number

    for songTitle in uniqueSongTitles:
        
        for i in range(number):
            if (topNSongsList[i][1] < songTimesPlayed.get(songTitle)):
                topNSongsList[i][1] = {songTitle, songTimesPlayed.get(songTitle)}



    print(topNSongsList)

    #plotTopSongsListened(topNSongsList)




#Plot the top 'number' of songs listened to
#topNSongs is a songHistory is dict of all songs, number is user input of desired X top songs
def plotTopSongsListened(topNSongs):

    plt.figure()

    #for i in range(topNSongsList):
     #   topNSongs[i] = 

    #Top number most listened songs, using iterator
    it = iter(songHistory)
    count = -1
    for song in range(number):

        count = count + 1
        #Get song title
        songTitle = next(it)

        #X-cords is song title, Y-cords is the value/number of times played
        plt.bar(songTitle, songHistory[count] )

        #Show number of times played on graph
        plt.text(song, songHistory[count], songHistory[count] ,color = 'blue', fontweight = 'bold')

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
    #print ('Total songs: ', len(songHistory))
    #uniqueSongs = set(songHistory)
    #print ('Total songs: ', len(uniqueSongs))

    menu()
    userChoice = int(input())
    

    while(userChoice != 4):
        #print("entered here")

        #Print top X songs
        if(userChoice == 1):
            topXSongs = int(input("Range of top songs?") )
            topSongsListenedTo(songHistory, topXSongs)


        #Print top songs listened by artist
        if(userChoice == 2):
            artistName = int(input("Name of artist?") )
            songsByArtist(songHistory, artistName)
            

        #Listening activity by month
        if(userChoice == 3):
            print()

        
        if(userChoice == 4):
            print()

        if(userChoice == 5):
            break

        else:
            print("Invalid input, Try again.")

        userChoice = input(menu())


    print("Program ended.")

     
main()