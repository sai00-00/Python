from tkinter import*
from PIL import Image, ImageTk
from pygame import mixer
import pygame
import random
from tkinter import filedialog

root = Tk()

mixer.init()

middleframe = Frame(root)
middleframe.grid(row=1,column=0)

play_frame = Frame(root)
play_frame.grid(row=2,column=0)

root.title("MyPlayer")
root.resizable(False,False)

def add_songs():
    songs = filedialog.askopenfilenames(initialdir='Music Player/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))   

    for song in songs:
        song = song.replace("C:/Songs", "")
        song = song.replace(".mp3", "")
        song = song.replace("C:/Users/Uttarkar Sai Nath/Desktop/Python/Music player/", "")

        songs_list.insert(END, song)

def exit():
    root.destroy()

def show_songs():
    return

def help_c():
    return

menu = Menu(root)

menu.add_command(label="Add Songs", command=add_songs)
menu.add_command(label="Show Songs", command=show_songs)
menu.add_command(label="Help", command=help_c)
menu.add_command(label="Exit", command=exit)

photo = PhotoImage(file='button.png')
stopphoto = PhotoImage(file='stop-button.png')
pausephoto = PhotoImage(file='pause.png')
previous = PhotoImage(file='back.png')
nextsong = PhotoImage(file='next.png')

songs_list = Listbox(middleframe, bg="white", fg="green", width=60, selectbackground="green", selectforeground="black")
songs_list.grid(row=0, column=0)

#global selected_song
#selected_song = random.choice(songs_list)

def play_btn():
    global stopped
    stopped = False

    song = songs_list.get(ACTIVE)
    song = f'C:/Users/Desktop/Python/Music Player/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop_btn():
    mixer.music.stop()
    print("Stop was clicked")

def set_vol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)
    print(volume, val)

if pygame.mixer.music.pause() == True:
    pause = False

elif pygame.mixer.music.unpause() == True:
    pause = True

a = 0

def pause():
    global index,a
    global pause
    a=a+1

    if pause == False:
        pygame.mixer.music.pause()
        pause = True
        print(pause,a)

    else:
        pygame.mixer.music.unpause()
        pause = False
        print(pause,a)

global index
index = 0

def next__song():
    return

def previous_song():
    return

#song_name = Label(middleframe, text="Now Playing "+str(songs_list[index]), font=('times','12','italic'))
#song_name.grid(row=1,column=0)

back_btn = Button(play_frame, image= previous, command=previous_song, relief=FLAT)
back_btn.grid(row=0,column=0)

stopbtn = Button(play_frame, image= stopphoto, command=stop_btn, relief=FLAT)
stopbtn.grid(row=0,column=1)

btn = Button(play_frame, image= photo, command=play_btn, relief=FLAT)
btn.grid(row=0,column=2)

pausebtn = Button(play_frame, image= pausephoto, command=pause, relief=FLAT)
pausebtn.grid(row=0,column=3)

frwd_btn = Button(play_frame, image= nextsong, command=next__song, relief=FLAT)
frwd_btn.grid(row=0,column=4)

scale = Scale(middleframe,from_ = 10, to = 120, orient= HORIZONTAL, command=set_vol, relief=FLAT)
scale.grid(row=2,column=0)

root.config(menu=menu)
root.mainloop()

