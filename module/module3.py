from tkinter import *   
import os # to acess lifes from computer using os
import glob # to find files of specific extension in an folder
import pygame # to implement playing of filesdance
import time # to intorduce delays
from mutagen.mp3 import MP3 # to get song length
  
top = Tk()

top.geometry("200x100")
canvas = Canvas()
canvas.create_line(300,550,2000,550)
canvas.create_line(300,0,300,2000)
canvas.create_line(0, 250, 300, 250,dash=(4,2))
canvas.pack(fill=BOTH, expand=1)
songarea = Text(top,width=30,height=20)
songarea.insert(INSERT,"HERE LIST OF SONG WILL BE DISPLAYED")
# songarea.insert(END," ")

lyricsarea = Text(top,width=100,height=30)
lyricsarea.insert(INSERT,"HERE LYRICS OF SONG")
lyricsarea.insert(END," WILL BE DISPLAYED")
lyricsarea.place(x=400 ,y=40)

heading = Label(top, text="AKATSUKI PLAYER!")
heading.place(x=700, y=10)
songlabel = Label(top, text="SONG LIST!")
songlabel.place(x=25, y=260)
buttonlabel= Label(top, text="BUTTONS!")
buttonlabel.place(x=350, y=555)


song_list = {}
pausepointer= 1
pointer = 1 # to asign an index to each song

path = input("Enter the folder that has your songs!! <3 \n ") # gets the input folder where songs resides
print(path)
songlistbox = Listbox(top)
songlistbox.place(x=20 ,y=300)  
   
for filename in glob.glob('*.mp3'): #loops through all the files in that folder with the extension ".mp3"
    #print("inside")
    with open(os.path.join(os.curdir, filename), 'r') as f:
       song_list[pointer]=filename # adding each song to the dict while assing it a unique ordered index value
       sl="\n"+str(pointer)+"-" + filename[:-4]
       songarea.insert(END,sl)
       songlistbox.insert(pointer, sl)
       print(str(pointer)+"-" + filename[:-4]) 
       pointer = pointer + 1 #incremneting the index of the song list after appending



song_index = int(input("Enter the no of the song u want to play!"))

song_tobeplayed= song_list[song_index]

# def fun():  
#     messagebox.showinfo("Hello", "Red Button clicked")
def playbutton(x=song_tobeplayed): # function to play a song
    global pausepointer
    pausepointer = 1
    pygame.mixer.init(44100, -16,2,2048)
    #pygame.mixer.music.stop()
    pygame.mixer.music.load(x)
    pygame.mixer.music.play(-1)
    #while pygame.mixer.music.get_busy():
    #    pygame.time.Clock().tick(10)

    print("playing 1 st song")
    #audio = MP3(x)
    #delay = (audio.info.length)
    #time.sleep(delay)
def pausebutton():
    global pausepointer
    if pausepointer ==0:
        pygame.mixer.music.unpause()
    elif pausepointer ==1:
        pygame.mixer.music.pause()
        pausepointer =0

def skipbutton():
    pausebutton()
    global song_index
    song_index = song_index +1
    song_tobeplayed= song_list[song_index]
    playbutton(song_tobeplayed)
    time.sleep(5)
    print("2nd song played")
  
b1 = Button(top,text = "PAUSE",command = pausebutton ,activeforeground = "red",activebackground = "pink",pady=10)
b1.place(x=400, y=600)

  
b2 = Button(top, text = "PLAY",command = playbutton , activeforeground = "black",activebackground = "pink",pady=10)
b2.place(x=500, y=600)
  
b3 = Button(top, text = "SKIP",command = skipbutton,activeforeground = "green",activebackground = "pink",pady = 10)
b3.place(x=600, y=600)

  
b4 = Button(top, text = "LYRICS",activeforeground = "yellow",activebackground = "pink",pady = 10)
b4.place(x=700, y=600)

#b1.pack(side = LEFT)  
  
#b2.pack(side = RIGHT)  
  
#b3.pack(side = TOP)  
  
#b4.pack(side = BOTTOM)




top.mainloop()