# Module -1
# 1/2/2020
#This modules lists out all the mp3 files in an folder

import os # to acess lifes from computer using os
import glob # to find files of specific extension in an folder
import pygame # to implement playing of files
import time # to intorduce delays
from playsound import playsound

def playbutton(x): # function to play a song
    playsound(x)


song_list = {}
pointer = 1 # to asign an index to each song

path = input("Enter the folder that has your songs!! <3 \n ") # gets the input folder where songs resides
for filename in glob.glob('*.mp3'): #loops through all the files in that folder with the extension ".mp3"
   with open(os.path.join(os.curdir, filename), 'r') as f:
       song_list[pointer]=filename # adding each song to the dict while assing it a unique ordered index value
       print(pointer , "-" , filename[:-4]) 
       pointer = pointer + 1 #incremneting the index of the song list after appending



song_index = int(input("Enter the no of the song u want to play!"))

song_tobeplayed= song_list[song_index]


#print(get_song ,song_tobeplayed)
playbutton(song_tobeplayed)









