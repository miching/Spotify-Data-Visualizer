#import matplotlib
import json

f = open('StreamingHistory0.json')
data = json.load(f)

for song in data['']:
    print(song['trackName'])

print("PRINT THIS", f.read())

#print("Hello World")