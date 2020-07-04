from youtube_transcript_api import YouTubeTranscriptApi
from datetime import date
import os

# Copy the URL of your desired YouTube video and set the URL
# variable below equal to the copied URL
# EX: URL = 'ThisIsYourVideosURL'

# Your YouTube video URL goes here:
URL = 'https://www.youtube.com/watch?v=v1I3inlM35k'

split_at = 'watch?v='

# Extracts the video ID from the URL
video_id = URL.partition(split_at)[2] 

# Uses a given function from the YouTube API to get
# the captions transcript of desired video
trans_list = YouTubeTranscriptApi.get_transcript(video_id)

# Takes the captions form the transcript and puts them into a list
captions = [ sub['text'] for sub in trans_list ]

# Gets the current date and formats it
today = date.today()
date = today.strftime("%b-%d-%Y")

# Set the defualt file name to
# 'Lecture_Today's Date.txt'
fileName = "Lecture_" + str(date) + ".txt"

# Joins a path to the users Documents folder
# to store the file in that folder
path_to_Docs = os.path.join(os.path.expanduser('~'), 'Documents', fileName)

# Creates and opens the file for writing
f = open(path_to_Docs,"w+")

# Counter that helps with formatting
lineCounter = 0

# Wites the captions in a formatted
#  way to the file
for caption in captions:
    lineCounter += 1
    f.write(str(caption) + ' ')
    
    if lineCounter == 10:
        f.write("\n")
        lineCounter = 0


# Closes the file
f.close() 


        