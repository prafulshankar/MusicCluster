import sys
import os
import glob
import scipy.io.wavfile

# standard thing to do for us would be to call parse('pydub_tests/*/*.wav')

def parse(pattern_match):
    file_list = glob.glob(pattern_match)
    data = []
    for filename in file_list:
        data_in_file = scipy.io.wavfile.read(filename)
        data.append(data_in_file[1])
    return data
