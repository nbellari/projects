#!/usr/bin/python
# This script converts a WMA file into a MP3 file.

# Requisites: mplayer lame
# Disclaimer: it worked last time I checked, but it was a long time ago,
#             so I put it here just to reference. Use it at your own risk.

import os

list = os.listdir(".")
for f in list:
    file = f.strip()
    if file.endswith(".wma") or file.endswith(".WMA"):
       print "converting",file
       new_file = file[:-3] + "mp3"
       command = "mplayer -ao pcm \"" + file + "\""
       print(command)
       os.system(command)
       command = "lame -b 128 audiodump.wav \"" + new_file + "\"";
       print(command)
       os.system(command)
       command = "rm audiodump.wav"
       print(command)
       os.system(command)
print "Finished. Bye, Bye"
