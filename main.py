import os
import graphicsToText
import speechToText
import recordUserSpeech
import compareTexts
import userSpeechToText
import time
from gtts import gTTS
from playsound import playsound

opt = input("\n\nHello! Welcome to retAIn! \n\nYou can upload a passage to revise in the following ways. \na) Paste Text b) Scan Image c) Upload Voice Note \nEnter your choice: ")
print("")

forc = ""
finalText = ""
# get reference material in text format
if (opt == "a"): # paste text
    finalText  = input("Enter text: ")
elif (opt == "b"):
    imgTitle = input("Enter PNG filename: ")
    finalText = graphicsToText.getGraphicsToText(imgTitle) # create in graphicsToText.py
elif (opt == "c"):
    wavTitle = input("Enter WAV filename: ")
    finalText = userSpeechToText.getUserSpeechToText(wavTitle) # create in speechToText.py
    forc = wavTitle
else:
    print("Bad input. Try again.\n\n")
    exit()

print("Document processed. Your text is now ready!")
readout = input("Would you like an audio of the document to be played (y/n)? ")
if (readout.lower() == "y"):
    if (opt == "c"):
        playsound(forc)
    else:
        myobj = gTTS(text=finalText, lang='en', slow=False)
        myobj.save("playsound.mp3")
        playsound("playsound.mp3")

ent = input("\nPress enter to begin recording.")

# get recording of user speaking  
recordUserSpeech.getUserRecording()

# convert user speech into text
generatedText = userSpeechToText.getUserSpeechToText('out2.wav')

# generate similarity score
similarityScore = compareTexts.getComparision(generatedText, finalText)

if (similarityScore > 7.5):
    similarityScore = 10 - (10 - similarityScore)/2
elif (similarityScore < 2):
    similarityScore = 0
elif (similarityScore < 5):
    similarityScore = similarityScore - 1
print("Your score is", round(similarityScore), "\b/10.\n\n")

# os.remove("out.wav")

