import sounddevice
from scipy.io.wavfile import write
import numpy as np
import wavio


def getUserRecording() :
    fs = 44100
    second = int(input("Enter time duration in seconds: "))
    print("Recording.....n")
    record_voice = sounddevice.rec( int ( second * fs ) , samplerate = fs , channels = 1, dtype=np.int16)

    sounddevice.wait()

    write('out.wav',fs,record_voice)
    wavio.write('out2.wav', record_voice, fs ,sampwidth=2)
    print("Finished")
