from youtube_transcript_api import YouTubeTranscriptApi
import os


# Takes in the video URL as input and
# extracts the video ID from the URL.
# Throws an error if it is an invalid
# YouTube URL, otherwise returns the video ID
def get_URL():

    URL = input("Enter your video's URL: ")

    # Every valid YouTube video URL should
    # contain this line. The video ID comes
    # after this line for every URL
    split_at = 'watch?v='


    if 'https://www.youtube.com/watch?v=' in URL:
        video_id = URL.partition(split_at)[2]
    else:
        raise Exception("This is not a valid video URL")
        
        
    return video_id


# Uses a given function from the YouTube API to get
# the captions transcript of the desired video.
# Throws an error if the video doesn't have a captions transcript,
# otherwise returns the captions as a list of words.
def get_transcript(vid_ID):

    try:
        transcript = YouTubeTranscriptApi.get_transcript(vid_ID)
    except:
        raise Exception("This video doesn't have a captions transcript")


    # Takes the captions from the transcript and puts them into a list
    # making a list of sentences.
    captions_list = [ sub['text'] for sub in transcript ]

    return captions_list


# Asks the user what they want the file to be named,
# makes the file a .txt file, and joins a path to the user's 
# 'Documents' folder to store the file in that folder.
# Returns the file with specified name
def make_file():

    file = input("\nWhat do you want the file to be called?: ")


    if ".txt" not in file:
        completeName = str(file) + ".txt"
    else:
        completeName = str(file)

    # Gets the file name without the extension
    name = os.path.splitext(completeName)[0]

    # Creates a path to the users Documents folder
    path_to_Docs = os.path.join(os.path.expanduser('~'), 'Documents', completeName)


    fileCounter = 1
    # Handles if there are duplicate file names
    while os.path.isfile(path_to_Docs):

        findName = completeName[0:len(name)]

        completeName = str(findName) + '(' + str(fileCounter) + ')' + '.txt'

        path_to_Docs = os.path.join(os.path.expanduser('~'), 'Documents', completeName)

        fileCounter += 1


    return path_to_Docs


# Creates and opens the file for writing,
# writes the captions in a formatted way to 
# the file, and then closes the file.
def format_file(file, captions):
    
    f = open(file, "w+")

    for caption in captions:

        f.write(str(caption) + ' ')
        f.write("\n")
        
    f.close()


# Main driver function that calls
# all the other functions.
def main():

    video_ID = get_URL()
    captions = get_transcript(video_ID)
    file = make_file()
    format_file(file, captions)


if __name__ == '__main__':
    main()

