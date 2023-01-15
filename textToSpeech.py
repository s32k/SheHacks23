# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
from playsound import playsound
# The text that you want to convert to audio
mytext = "Eeshita is tall. Eeshita has medium-length hair. Eeshita has a very pretty smile. Eeshita's thumbs can do 'this'. Eeshita wears glasses. Byee."

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
playsound("welcome.mp3")
# os.system("mpg321 welcome.mp3")