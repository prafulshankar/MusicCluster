import midi
import os
import sys

directory_name = sys.argv[1]
new_directory_name = sys.argv[2]

files_to_convert = os.listdir(directory_name)
for fil in files_to_convert:
    filename = directory_name + '/' + fil
    filepat = midi.read_midifile(filename)
    destfile = new_directory_name + '/' + fil + ".txt"
    dest = open(destfile, 'w')
    dest.write(str(filepat))
