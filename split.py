import midi
import sys
import pydub
import os
import scipy

# convert all files in directory to split mp3s
directory_name = sys.argv[1]
print directory_name

if directory_name[-1] != "/":
    directory_name += "/"

files_to_conv = os.listdir(directory_name)
files_to_convert = [each for each in files_to_conv if each[-3:]=="mp3"]
print files_to_convert

def export_mp3_parts(destfile, audio):
    def song_split(song):
        length = len(song)
        splits = [0.2*length, 0.4*length, 0.6*length, 0.8*length, length]
        splits = [song[:0.2*length], song[0.2*length:0.4*length], song[0.4*length:0.6*length], song[0.6*length:0.8*length], song[0.8*length:]]
        return [part[(len(part)//2)-5000:(len(part)//2)+5000] for part in splits]
    
    split_sound = song_split(audio)
        
    for part in range(len(split_sound)):
        split_sound[part].export(destfile[0:-4] + "_" + str(part+1) + ".wav",
            format = "wav")

for fil in files_to_convert:
    path = directory_name + fil[0:-4]
    if not os.path.exists(path):
        os.makedirs(path)
    source_fil = directory_name + fil
    dest_fil = path + "/" + fil
    print source_fil, dest_fil
    mp3_audio = pydub.AudioSegment.from_file(source_fil, "mp3")
    
    export_mp3_parts(dest_fil, mp3_audio)
