# Kay_JEY / 25-3-21 /
from tkinter import *   
from tkinter import filedialog
from PIL import *

iconimage = 'images/yellowhead.ico'
bgimage='images/bg1.png'
#import os # to acess lifes from computer using os
#import glob # to find files of specific extension in an folder
import pygame # to implement playing of filesdance
#import time # to intorduce delays
#from mutagen.mp3 import MP3 # to get song length

root = Tk()
root.title('AKATSUI PLAYER')
root.geometry('1200x1000')
root.config(bg= 'black')
root.iconbitmap(iconimage)

bg=PhotoImage(file=bgimage)

bg_label= Label(root,image=bg)
bg_label.place(x=0, y=0)


def browsefiles():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)

def pausebutton():
    return

def playbutton(): # function to play a song
    global pausepointer
    pausepointer = 1
    pygame.mixer.init(44100, -16,2,2048)
    #pygame.mixer.music.stop()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(-1)



#Cretaing menubar
menubar = Menu(root)
root.config(menu=menubar)

#creating submenu called FILE
subMenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "FILE", menu = subMenu)
subMenu.add_command(label = "OPEN", command = browsefiles)
subMenu.add_command(label = "EXIT",command = root.destroy)
#creating submenu called HELP
subMenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "HELP", menu = subMenu)
subMenu.add_command(label = "About Us")
subMenu.add_command(label = "Reach Us")

b1 = Button(root,text = "PAUSE",command = pausebutton ,activeforeground = "red",activebackground = "pink",pady=20, padx = 10)
b1.place(x=400, y=600)

  
b2 = Button(root, text = "PLAY",command = playbutton , activeforeground = "black",activebackground = "pink",pady = 20, padx = 10)
b2.place(x=500, y=600)
  
b3 = Button(root , text = "SKIP", pady = 20, padx = 10)
b3.place(x= 600, y=600)

  
b4 = Button(root, text = "LYRICS",activeforeground = "yellow",activebackground = "pink",pady = 20, padx = 10)
b4.place(x=700, y=600)





root.mainloop()