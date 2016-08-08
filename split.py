import midi
import sys
import pydub
import os

directory_name = sys.argv[1]
print directory_name
files_to_conv = os.listdir(directory_name)
files_to_convert = [each for each in files_to_conv if each[-3:]=="mp3"]
print files_to_convert

def export_mp3_parts(filename, audio):
	def song_split(song):
		length = len(song)
		splits = [0.2*length, 0.4*length, 0.6*length, 0.8*length, length]
		splits = [song[:0.2*length], song[0.2*length:0.4*length], song[0.4*length:0.6*length], song[0.6*length:0.8*length], song[0.8*length:]]
		return [part[(len(part)//2)-5000:(len(part)//2)+5000] for part in splits]
	
	split_sound = song_split(audio)
		
	for part in range(len(split_sound)):
		split_sound[part].export(filename[0:-4] + "_" + str(part+1) + ".mp3")

for fil in files_to_convert:
	fil = directory_name +  "/" + fil
	print fil
 	mp3_audio = pydub.AudioSegment.from_file(fil, "mp3")
	export_mp3_parts(fil, mp3_audio)