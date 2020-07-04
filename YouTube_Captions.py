from youtube_transcript_api import YouTubeTranscriptApi
from datetime import date
import sys
import os


# Copy the URL of your desired YouTube video
# and paste it into the command line when prompted

# Takes in the video URL as input
URL = input("Paste the video URL here: ")

split_at = 'watch?v='

# Extracts the video ID from the URL,
# throws an error if it is an invalid
# YouTube URL
if 'https://www.youtube.com/watch?v=' in URL:
    video_id = URL.partition(split_at)[2]
else:
    print("ERROR: This is not a valid YouTube URL")
    sys.exit(0)


# Uses a given function from the YouTube API to get
# the captions transcript of the desired video,
# throws an error if the video doesn't have a captions transcript
try:
    captions_list = YouTubeTranscriptApi.get_transcript(video_id)
except:
    print("ERROR: This video doesn't have captions")
    sys.exit(0)


# Takes the captions form the transcript and puts them into a list
captions = [ sub['text'] for sub in captions_list ]


# Gets the current date and formats it
today = date.today()
date = today.strftime("%b-%d-%Y")


# Sets the defualt file name to
# 'Lecture_Today's Date.txt'
fileName = "Lecture_" + str(date) + ".txt"


# Joins a path to the users Documents folder
# to store the file in that folder
path_to_Docs = os.path.join(os.path.expanduser('~'), 'Documents', fileName)


# Creates and opens the file for writing
f = open(path_to_Docs, "w+")


# Counter that helps with formatting
lineCounter = 0

# Wites the captions in a formatted
#  way to the file
for caption in captions:
    lineCounter += 1
    f.write(str(caption) + ' ')
    
    if lineCounter == 8:
        f.write("\n")
        lineCounter = 0


# Closes the file
f.close() 


        
        