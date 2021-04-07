# Module -1
# 1/2/2020
#This modules lists out all the mp3 files in an folder

import os # to acess lifes from computer using os
import glob # to find files of specific extension in an folder
import pygame # to implement playing of filesdance
import time # to intorduce delays
from mutagen.mp3 import MP3 # to get song length





def playbutton(x): # function to play a song
    pygame.mixer.init(44100, -16,2,2048)
    #pygame.mixer.music.stop()
    pygame.mixer.music.load(x)
    pygame.mixer.music.play(-1)
    #while pygame.mixer.music.get_busy():
    #    pygame.time.Clock().tick(10)

    print("playing 1 st song")
    audio = MP3(x)
    delay = (audio.info.length)
    #time.sleep(delay)

def pausebutton():
    pygame.mixer.pause()

def skipbutton():
    pausebutton()
    global song_index
    song_index = song_index +1
    song_tobeplayed= song_list[song_index]
    playbutton(song_tobeplayed)
    time.sleep(5)
    print("2nd song played")



song_list = {}
pointer = 1 # to asign an index to each song

path = input("Enter the folder that has your songs!! <3 \n ") # gets the input folder where songs resides
print(path)
for filename in glob.glob('*.mp3'): #loops through all the files in that folder with the extension ".mp3"
    print("inside")
    with open(os.path.join(os.curdir, filename), 'r') as f:
       song_list[pointer]=filename # adding each song to the dict while assing it a unique ordered index value
       print(pointer , "-" , filename[:-4]) 
       pointer = pointer + 1 #incremneting the index of the song list after appending



song_index = int(input("Enter the no of the song u want to play!"))

song_tobeplayed= song_list[song_index]


#print(get_song ,song_tobeplayed)
playbutton(song_tobeplayed)
time.sleep(5)
print("SONG Paused")
skipbutton()

#pausebutton()









