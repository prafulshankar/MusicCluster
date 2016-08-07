import midi
import sys
import pydub
import os

directory_name = sys.argv[1]

files_to_convert = os.listdir(directory_name)

def export_mp3_parts(filename, audio):
	def song_split(song):
		length = len(song)
		splits = [0.2*length, 0.4*length, 0.6*length, 0.8*length, length]
		splits = [song[:0.2*length], song[0.2*length:0.4*length], song[0.4*length:0.6*length], song[0.6*length:0.8*length], song[0.8*length:]]
		return [part[(len(sound)//2)-5000:(len(part)//2)+5000] for part in splits]
	
	split_sound = sound_split(audio)
	
	for part in range(len(split_sound)):
		split_sound[part].export(filename[0:-4] + str(part) + ".mp3")

for fil in files_to_convert:
	print fil
 	mp3_audio = pydub.AudioSegment.from_file(fil, "mp3")
	export_mp3_parts(fil, mp3_audio)