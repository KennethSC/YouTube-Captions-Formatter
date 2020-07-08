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


    # Takes the captions_list above and turns it from a list of 
    # sentences to a list of words.
    captions = [word for line in captions_list for word in line.split()]

    return captions


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


    path_to_Docs = os.path.join(os.path.expanduser('~'), 'Documents', completeName)

    return path_to_Docs


# Creates and opens the file for writing,
# writes the captions in a formatted way to 
# the file, and then closes the file.
def format_file(file, captions):
    
    f = open(file, "w+")

    # Counter that helps with formatting
    wordCounter = 0

    for caption in captions:
        wordCounter += 1

        f.write(str(caption) + ' ')
        
        if wordCounter == 11:
            f.write("\n")
            wordCounter = 0

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

