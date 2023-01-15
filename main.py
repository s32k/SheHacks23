import os
import graphicsToText
import speechToText
import recordUserSpeech
import compareTexts
import userSpeechToText
import time

opt = input("Hello! Welcome to retAIn. Choose a way to upload text: \n a) paste text b) scan image c) upload voice note \n")

# get reference material in text format
if (opt == "a"): # paste text
    finalText  = input("Enter text: ")
elif (opt == "b"):
    imgTitle = input("Enter PNG filename: ")
    finalText = graphicsToText.getGraphicsToText(imgTitle) # create in graphicsToText.py
elif (opt == "c"):
    wavTitle = input("Enter WAV filename: ")
    finalText = speechToText.getSpeechToText(wavTitle) # create in speechToText.py
else:
    print("Bad input. Try again.")
    exit()

print("Document processed. Your text is now ready: ")
print(finalText)

ent = input("Press enter to begin recording.")

# get recording of user speaking  
recordUserSpeech.getUserRecording()

# convert user speech into text
print('convert user speech into text')
generatedText = speechToText.getSpeechToText("out2.wav")
print('convert user speech into text DONE!!')

# generate similarity score
similarityScore = compareTexts.getComparision(generatedText, finalText)
print("Your score is " + similarityScore + "/100.")

# os.remove("out.wav")

