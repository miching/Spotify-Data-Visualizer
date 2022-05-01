#import matplotlib
import json

with open ('StreamingHistory0.json') as f:
    data = json.load(f)

#f = open('StreamingHistory0.json')
#data = json.load(f)

for song in data:
    print(song['trackName'])

#print("PRINT THIS", f.read())

#print("Hello World")