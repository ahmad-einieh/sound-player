import pygame
import tkinter
from tkinter import *
from tkinter.filedialog import askdirectory
import os

win = Tk()
win.title("Music Player")
win.geometry("450x350")
#
dir=askdirectory()
os.chdir(dir)
songlist = os.listdir()
playlist = Listbox(win, font="Cambria 15 bold",bg="cyan2",selectmod=SINGLE)

for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos +=1

pygame.init()
pygame.mixer.init()

var = StringVar()

def play():
    pygame.mixer.music.load(playlist.get(ACTIVE))
    var.set(playlist.get(ACTIVE))
    pygame.mixer.music.play()

def exitmusicplayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

# buttons
play_b =Button(win,height=3,width=5,text="Play Music",font="Cambria 15 bold",command=play,bg='lime green',fg='black')
play_b.pack(fill='x')
play_b1 =Button(win,height=3,width=5,text="Stop Music",font="Cambria 15 bold",command=exitmusicplayer,bg='red',fg='black')
play_b1.pack(fill='x')
play_b2 =Button(win,height=3,width=5,text="Pause Music",font="Cambria 15 bold",command=pause,bg='yellow',fg='black')
play_b2.pack(fill='x')
play_b3 =Button(win,height=3,width=5,text="Resume Music",font="Cambria 15 bold",command=resume,bg='yellow',fg='black')
play_b3.pack(fill='x')

playlist.pack(fill='both',expand='yes')


win.mainloop()