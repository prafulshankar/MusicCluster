from parser import *

songs = parse('*/*/*.wav')

songToParse = songs[0]
kparam = 2
for i in range(len(songToParse)/kparam):
    acc = [0,0]
    for j in range(kparam):
        acc += songToParse[(kparam * i) + j]
    acc /= kparam
    for j in range(kparam):
        songToParse[(kparam * i) + j] = acc

scipy.io.wavfile.write('check.wav', 44100, songToParse)
