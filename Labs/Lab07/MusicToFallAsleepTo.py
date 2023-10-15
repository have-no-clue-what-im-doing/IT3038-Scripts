import winsound
import random

def MusicPlayer(freq):
    winsound.Beep(freq, 500)
    
def FreqChanger():
    freq = 37
    while True:
        if freq >= 12000:
            freq = 37
        else:
            freq += 100
        MusicPlayer(freq)

FreqChanger()

def GoingDeaf():
    while True:
        winsound.Beep(10000, 100000)

#GoingDeaf()

def PitchPerfect():
    while True:
        randomFreq = random.randrange(37, 10000)
        randomTime = random.randrange(10, 1000)
        winsound.Beep(randomFreq, randomTime)
        PitchPerfect()

PitchPerfect()

