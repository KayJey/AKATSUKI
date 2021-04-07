# Module -2
# 6/2/2021
#Front-end of the application 

from  tkinter import *


#root
root = Tk()
root.configure(background='#7fe8f9')

#functions
def pause_but():
    return

def play_but():
    return


#componenets
myLabel = Label(root, text = "AKATSUKI PLAYER")
pause_button = Button(root, text = "PAUSE", command = pause_but, bg="#fa454a" , fg = "white") # (use padx , pady for button size; stae= ENABLED/DISABLED) 
play_button = Button(root, text = "PLAY",bg="#fa454a" , fg = "white")
folderloc= Entry(root,)

#packing / grid spacing 
myLabel.pack()
pause_button.pack()
play_button.pack()



#main loop
root.mainloop()

