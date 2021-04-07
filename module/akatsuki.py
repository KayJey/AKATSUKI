

import os
import glob
import pygame
import time

path = "D:\projects\python\sem_6\miniprojec"
for filename in glob.glob('*.mp3'):
   with open(os.path.join(os.curdir, filename), 'r') as f:
       print(filename)

def playbutton(S):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(S)
    pygame.mixer.music.play()

print("\n\n ")
pygame.mixer.init(44100, -16,2,2048)

pygame.mixer.music.load("3.mp3")
pygame.mixer.music.play()
playbutton("2.mp3")

time.sleep(5)



