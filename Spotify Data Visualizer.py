#import matplotlib as plt
from ctypes import alignment
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




# Count how much times a song has been played
# Returns a dict with key-value of {songTitle: timesPlayed}
def countTimesPlayed(songHistory):

    songTimesPlayed = {}
    allSongTitles = [song['trackName'] for song in songHistory]
    uniqueSongTitles = set(allSongTitles)

    for songTitles in uniqueSongTitles:
        songTimesPlayed[songTitles] = allSongTitles.count(songTitles)


    return (songTimesPlayed)

    

# Get top range of songs listened to
def topSongsListenedTo(songHistory, topRange):

    # List to hold top N songs
    topSongsList = []

    # Dict holding {songTitle: timesPlayed}
    songTimesPlayed = countTimesPlayed(songHistory)

    # Sort by most played to least played songs
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

    # Hold song titles for x-Axis
    xAxisTitles = []

    # For each top song, plot with bar graph
    for i in range(len(topSongsList)):
        song = topSongsList[i]
        songTitle = song[0]
        songCount = song[1]

        xAxisTitles.append(songTitle)

        #X-cords is song title, Y-cords is the value/number of times played
        plt.bar(songTitle, songCount)

        #Show number of times played on graph
        plt.text(songTitle, songCount, songCount ,color = 'blue', fontweight = 'bold')

        
    # x-Axis Labels    
    plt.xticks(xAxisTitles)

    #Display bar graph
    plt.show()




# Get songs created by artist
def songsByArtist(songHistory, artistName):

    # List of dicts that hold songs created by artist
    songsByArtistList = []

    # For all songs listned to
    for i in range(len(songHistory)):
        if(songHistory[i]['artistName'] == artistName):
            songsByArtistList.append(songHistory[i])


    # No songs were played that were created by artistName
    if(len(songsByArtistList) == 0):
        print('No songs played by artist ' + artistName)

    else:

        # Dict holding {songTitle: timesPlayed}
        songTimesPlayed = countTimesPlayed(songsByArtistList)

        # Sort by most played to least played songs
        songTimesPlayed = sorted(songTimesPlayed.items(), key=lambda x: x[1], reverse=True)

        #print(songTimesPlayed)
        plotSongsByArtist(songTimesPlayed, artistName)
        


# Plot songs created by artist
# artistSongList is a list of tuples in the form (songTitle, timesPlayed)
def plotSongsByArtist(artistSongList, artistName):

    totalTimesPlayed = 0

    plt.figure()
    plt.title("Your most listened songs by artist " + artistName)
    plt.xlabel("Song(s)")
    plt.ylabel("Times played")

    # Hold song titles for x-Axis
    xAxisTitles = []

    # For each top song, plot with bar graph
    for i in range(len(artistSongList)):
        song = artistSongList[i]
        songTitle = song[0]
        songCount = song[1]
        totalTimesPlayed = totalTimesPlayed + songCount

        xAxisTitles.append(songTitle)

        #X-cords is song title, Y-cords is the value/number of times played
        plt.bar(songTitle, songCount)

        #Show number of times played on graph
        plt.text(songTitle, songCount, songCount ,color = 'blue', fontweight = 'bold')

        
    # x-Axis Labels    
    #plt.xticks(xAxisTitles)

    print('Total songs played by artist ' + artistName + ': ' + str(totalTimesPlayed) )

    #Display bar graph
    plt.show()



# Get top range of artists listened to
def topArtistsListenedTo(songHistory, topRange):
    print()



# Plot the top artists listened to
def plotTopArtists(artistsList):
    print()



def menu():
    print("1) Top songs listened to")
    print("2) Top songs listened to by an artist")
    print("3) Most listened artists")
    print("4) Exit.")



def testmain():
    print("Hello world")

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
        if(userChoice == 2):
            artistName = int(input("Name of artist?") )
            songsByArtist(songHistory, artistName)
            

        # Most listened artists
        if(userChoice == 3):
            rangeTopArtists = int(input("Range of top artists listned to?") )
            topSongsListenedTo(songHistory, rangeTopArtists)

        
        if(userChoice == 4):
            print()

        if(userChoice == 5):
            break

        else:
            print("Invalid input, Try again.")

        userChoice = input(menu())


    print("Program ended.")


def main():
    songHistory = readSongHistory()
    #countTimesPlayed(songHistory)
    topSongsListenedTo(songHistory, 5)
    #allSongsListened(songHistory)
    #songsByArtist(songHistory, 'Post Malone')
    #songsByArtist(songHistory, 'gfdgfd')

if __name__ == '__main__':    
    main()