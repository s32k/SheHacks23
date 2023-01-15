import speech_recognition as sr

def getSpeechToText(wavTitle):
    filename = wavTitle

    # initialize the recognizer
    r = sr.Recognizer()

    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, show_all=True)

        print (" TEXT !!!!!!!")
        print (text)
        return (text['alternative'][0]['transcript'])
