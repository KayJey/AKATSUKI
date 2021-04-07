# Kay_JEY / 25-3-21 /
from tkinter import *  
from tkinter import messagebox
from tkinter import filedialog
from PIL import *
import pygame


pausepointer =0
iconimage = 'images/yellowhead.ico'
bgimage='images/bg2.png'


def browsefiles():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)

def pausebutton():
    global pausepointer
    if pausepointer ==0:
        pygame.mixer.music.unpause()
        pausepointer =1
    elif pausepointer ==1:
        pygame.mixer.music.pause()
        pausepointer =0

def playbutton(): # function to play a song
    try:
        global pausepointer
        pausepointer = 1
        pygame.mixer.init(44100, -16,2,2048)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(-1)
    except:
        messagebox.showerror('file not found','Akatsuki cant find the files')
        print("PLAY ERROR")

root = Tk()
root.title('AKATSUI PLAYER')
root.geometry('1000x1000')
root.config(bg= 'black')
root.iconbitmap(iconimage)
bg=PhotoImage(file=bgimage)

#creating frames
leftframe = Frame(root)
leftframe.pack()

rightframe = Frame(root)
rightframe.pack()


brFrame = Frame(rightframe)

mycanvas = Canvas(root, width = 10, height =10)
mycanvas.pack(fill='both', expand=True)
mycanvas.create_image(0,0 ,image=bg)

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

b1 = Button(brFrame,text = "PAUSE",command = pausebutton ,activeforeground = "purple",activebackground = "black",pady=20, padx = 10)
b1_win = mycanvas.create_window( window = b1)
b2 = Button(root, text = "PLAY",command = playbutton , activeforeground = "purple",activebackground = "black",pady = 20, padx = 10)
b2_win = mycanvas.create_window(500, 600, window = b2)
b3 = Button(root , text = "SKIP",activeforeground = "purple",activebackground = "black" ,pady = 20, padx = 10)
b3_win = mycanvas.create_window(600, 600, window = b3)
b4 = Button(root, text = "LYRICS",activeforeground = "purple",activebackground = "black",pady = 20, padx = 10)
b4_win = mycanvas.create_window(700, 600, window = b4)

LB = Listbox(root)



root.mainloop()
