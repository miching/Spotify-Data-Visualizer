#import matplotlib as plt
from ctypes import alignment
from re import T
from tkinter import CENTER
from xmlrpc.client import boolean
from matplotlib import ticker
import matplotlib.pyplot as plt
import json
from collections import Counter

# Read all JSON files and transform into dict 
def readSongHistory():
    readAllFiles = True
    amountOfFiles = 0
    data = {}
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
            #print("Cannot read file")
        #Print all music streams
        #for song in data:
        #    print (song)
        
        #print(data)
        #print(data[len(data)-1])
        return data
            


# Plot all songs
def allSongsListened(songHistory):

    songTimesPlayed = countTimesPlayed(songHistory)

    # Sort by most played to least played songs
    songTimesPlayed = sorted(songTimesPlayed.items(), key=lambda x: x[1], reverse=True)

    plotTopSongsListened(songTimesPlayed)




# Count how many times a song has been played
# Returns a dict with key-value of {songTitle: timesPlayed}
def countTimesPlayed(songHistory):

    songTimesPlayed = {}

    # For each song in songHistory, get trackName
    allSongTitles = [song['trackName'] for song in songHistory]

    # Make a set to discard repeat songTitles
    uniqueSongTitles = set(allSongTitles)

    for songTitles in uniqueSongTitles:
        songTimesPlayed[songTitles] = allSongTitles.count(songTitles)


    #print(songTimesPlayed)
    return (songTimesPlayed)

    

# Count how many times an artist has been listened to 
# Returns a dict with key-value of {artistName: timesPlayed}
def countArtistsPlayed(songHistory):

    artistTimesPlayed = {}

    # For each song in songHistory, get artistName
    allArtists = [song['artistName'] for song in songHistory]

    # Make a set to discard same artists
    uniqueArtists = set(allArtists)

    for artist in uniqueArtists:
        artistTimesPlayed[artist] = allArtists.count(artist)


    #print(artistTimesPlayed)
    return (artistTimesPlayed)



# Get top range of songs listened to
def topSongsListenedTo(songHistory, topRange):

    # List to hold top N songs
    topSongsList = []

    # Dict holding {songTitle: timesPlayed}
    songTimesPlayed = countTimesPlayed(songHistory)

    # Sort by most played to least played songs into a list
    songTimesPlayed = sorted(songTimesPlayed.items(), key=lambda x: x[1], reverse=True)

    # Requested range of top songs is out of size
    if(topRange > len(songTimesPlayed)):
        print('Range is beyond total songs listened')
    
    else:

        # For the range of top songs, add to list
        for i in range(topRange):
            topSongsList.append(songTimesPlayed[i])


        #print(songTimesPlayed)
        #print(topSongsList)

        plotTopSongsListened(topSongsList)



# Plot the top N of songs listened to
# topSongsList is a list of sorted tuples in the form (songTitle, timesPlayed)
def plotTopSongsListened(topSongsList):

    plt.figure()
    plt.title("Top " + str(len(topSongsList)) + " songs listened to")
    plt.xlabel("Song(s)")
    plt.ylabel("Times played")


    # For each top song, plot with bar graph
    for i in range(len(topSongsList)):
        song = topSongsList[i]
        songTitle = song[0]
        songCount = song[1]

        #X-cords is song title, Y-cords is the value/number of times played
        plt.bar(songTitle, songCount)

        #Show number of times played on graph
        plt.text(songTitle, songCount, songCount ,color = 'blue', fontweight = 'bold', ha = CENTER)

    
    # To prevent clutter, do not plot song titles if more 15
    if (len(topSongsList) > 15):
        plt.xticks([])

    #Display bar graph
    plt.show()




# Get songs created by artist
def songsByArtist(songHistory, artistName):

    # List of dicts that hold songs created by artist
    songsByArtistList = []

    # For all songs listned to, find songs by artistName
    for i in range(len(songHistory)):
        if(songHistory[i]['artistName'] == artistName):
            songsByArtistList.append(songHistory[i])


    # No songs were played that were created by artistName
    if(len(songsByArtistList) == 0):
        print('No songs played by artist ' + artistName)

    else:

        # Dict holding {songTitle: timesPlayed}
        songTimesPlayed = countTimesPlayed(songsByArtistList)

        # Sort by most played to least played songs into a list
        songTimesPlayed = sorted(songTimesPlayed.items(), key=lambda x: x[1], reverse=True)

        #print(songTimesPlayed)
        plotSongsByArtist(songTimesPlayed, artistName)
        


# Plot songs created by artist
# artistSongList is a list of tuples in the form (songTitle, timesPlayed)
def plotSongsByArtist(artistSongList, artistName):

    totalTimesPlayed = 0

    plt.figure()
    plt.title("Your most listened songs by artist " + artistName)
    plt.xlabel("Song Title")
    plt.ylabel("Times played")


    # For each top song, plot with bar graph
    for i in range(len(artistSongList)):
        song = artistSongList[i]
        songTitle = song[0]
        songCount = song[1]
        totalTimesPlayed = totalTimesPlayed + songCount

        #X-cords is song title, Y-cords is the value/number of times played
        plt.bar(songTitle, songCount)

        #Show number of times played on graph
        plt.text(songTitle, songCount, songCount ,color = 'blue', fontweight = 'bold', ha = CENTER)

        
    # To prevent clutter, do not plot song titles if more 15
    if (len(artistSongList) > 15):
        plt.xticks([])


    print('Total songs played by artist ' + artistName + ': ' + str(totalTimesPlayed) )

    #Display bar graph
    plt.show()



# Get top range of artists listened to
def topArtistsListenedTo(songHistory, topRange):

    # List to hold top N artists
    topArtistsList = []

    # Dict holding {artistName, timesPlayed}
    artistTimesPlayed = countArtistsPlayed(songHistory)

    # Sort by most played to least played artists into a list
    artistTimesPlayed = sorted(artistTimesPlayed.items(), key=lambda x: x[1], reverse=True)

    # Requested range of top songs is out of size
    if(topRange > len(artistTimesPlayed)):
        print('Range is beyond total artists listened')
    
    else:

        # For the range of top artists, add to list
        for i in range(topRange):
            topArtistsList.append(artistTimesPlayed[i])


        #print(artistTimesPlayed)
        #print(topArtistsList)

        plotTopArtists(topArtistsList)



# Plot the top artists listened to
# artistList is a list of tuples in the form (artistName, timesPlayed)
def plotTopArtists(artistsList):

    plt.figure()
    plt.title("Top " + str(len(artistsList)) + " artists listened to")
    plt.xlabel("Artist(s)")
    plt.ylabel("Times played")


    # For each top song, plot with bar graph
    for i in range(len(artistsList)):
        artistInfo = artistsList[i]
        artistName = artistInfo[0]
        timesPlayed = artistInfo[1]

        #X-cords is artist name, Y-cords is the number of times played
        plt.bar(artistName, timesPlayed)

        #Show number of times played on graph
        plt.text(artistName, timesPlayed, timesPlayed ,color = 'blue', fontweight = 'bold', ha = CENTER)

    
    # To prevent clutter, do not plot song titles if more 15
    if (len(artistsList) > 15):
        plt.xticks([])

    #Display bar graph
    plt.show()



# Print options for user to choose
def menu():
    print("1) Top songs listened to")
    print("2) Top songs listened to by an artist")
    print("3) Most listened artists")
    print("4) Exit.")



def main():
    #print("Hello world")

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

        # Print top X songs
        if(userChoice == 1):
            rangeTopSongs = int(input("Range of top songs listned to?") )
            topSongsListenedTo(songHistory, rangeTopSongs)
           

        # Print top songs listened by artist
        elif(userChoice == 2):
            artistName = input("Name of artist?") 
            songsByArtist(songHistory, artistName)
            

        # Most listened artists
        elif(userChoice == 3):
            rangeTopArtists = int(input("Range of top artists listned to?") )
            topArtistsListenedTo(songHistory, rangeTopArtists)
            menu()
            userChoice = int(input())

        
        elif(userChoice == 4):
            print('Exit')

        # Bad input
        else:
            print("Invalid input, Try again.")

        userChoice = input(menu())


    print("Program ended.")


def testMain():
    songHistory = readSongHistory()
    #countTimesPlayed(songHistory)
    #topSongsListenedTo(songHistory, 5)
    #allSongsListened(songHistory)
    #songsByArtist(songHistory, 'Post Malone')
    #songsByArtist(songHistory, 'Taylor Swift')
    #songsByArtist(songHistory, 'gfdgfd')
    #countArtistsPlayed(songHistory)
    #topArtistsListenedTo(songHistory, 5)

if __name__ == '__main__':    
    main()