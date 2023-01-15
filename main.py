import os
import graphicsToText
import speechToText
import recordUserSpeech
import compareTexts
import userSpeechToText
import time

opt = input("\nHello! Welcome to retAIn! \n\nYou can upload a passage to revise in the following ways. \na) Paste Text b) Scan Image c) Upload Voice Note \nEnter your choice: ")
print("\n")

# get reference material in text format
if (opt == "a"): # paste text
    finalText  = input("Enter text: ")
elif (opt == "b"):
    imgTitle = input("Enter PNG filename: ")
    finalText = graphicsToText.getGraphicsToText(imgTitle) # create in graphicsToText.py
elif (opt == "c"):
    wavTitle = input("Enter WAV filename: ")
    finalText = userSpeechToText.getUserSpeechToText(wavTitle) # create in speechToText.py
else:
    print("Bad input. Try again.")
    exit()

print("Document processed. Your text is now ready!")

ent = input("\nPress enter to begin recording.")

# get recording of user speaking  
recordUserSpeech.getUserRecording()

# convert user speech into text
generatedText = userSpeechToText.getUserSpeechToText('out2.wav')

# generate similarity score
similarityScore = compareTexts.getComparision(generatedText, finalText)
print("Your score is", int(10 - (10 - similarityScore)/2), "\b/10.\n")

# os.remove("out.wav")

