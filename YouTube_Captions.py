from youtube_transcript_api import YouTubeTranscriptApi
import sys
import os


# Copy the URL of your desired YouTube video
# and paste it into the command line when prompted

# Takes in the video URL as input
URL = input("Enter your video's URL: ")


split_at = 'watch?v='

# Extracts the video ID from the URL,
# throws an error if it is an invalid
# YouTube URL
if 'https://www.youtube.com/watch?v=' in URL:
    video_id = URL.partition(split_at)[2]
else:
    print("ERROR: This is not a valid YouTube URL.")
    sys.exit(0)


# Uses a given function from the YouTube API to get
# the captions transcript of the desired video,
# throws an error if the video doesn't have a captions transcript
try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
except:
    print("ERROR: This video doesn't have captions.")
    sys.exit(0)


# Takes the captions from the transcript and puts them into a list
# making a list of sentences.
captions_list = [ sub['text'] for sub in transcript ]

# Takes the captions_list above and turns it from a list of 
# sentences to a list of words.
captions = [word for line in captions_list for word in line.split()]


# Asks the user what they want the file to be named
file = input("\nWhat do you want the file to be called?: ")

# Makes the file a .txt file
completeName = str(file) + ".txt"


# Joins a path to the user's Documents folder
# to store the file in that folder
path_to_Docs = os.path.join(os.path.expanduser('~'), 'Documents', completeName)


# Creates and opens the file for writing
f = open(path_to_Docs, "w+")


# Counter that helps with formatting
wordCounter = 0

# Writes the captions in a formatted
# way to the file
for caption in captions:
    wordCounter += 1

    f.write(str(caption) + ' ')
    
    if wordCounter == 11:
        f.write("\n")
        lineCounter = 0


# Closes the file
f.close() 
