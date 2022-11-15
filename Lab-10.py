from gtts import gTTS
import os
import json

# Define dictonary
d = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot',
   'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',

   'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec', 'r': 'romeo',

   's': 'sierra', 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey',

   'x': 'x-ray', 'y': 'yankee', 'z': 'zulu', ' ': ' '}


# Function will take 2 parameters, and convert string into ICAO using dictionary which we pass as an argument

def stringToICAO(name,dict):
    convertedName = ""
    for i in name:
        convertedName = convertedName + dict[i.lower()] + " "
    return convertedName

# Open file and read file
file = open("lab-10.txt", "r")
fileText = file.read()

# Create string with original text as well as converted text
fileText = "Original text " + fileText + "converted text " + stringToICAO(fileText,d)

# Covert text file into speach file
myobj = gTTS(text=fileText, lang='en', slow=True)

# Save in .mp3 file
myobj.save("name.mp3")

