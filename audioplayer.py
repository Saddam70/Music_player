from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, filedialog
import os
from pygame import mixer
from tkinter import messagebox
import time
from mutagen.mp3 import MP3

# all colors
co1 = "#ffffff"  # white
co2 = "#3C1DC6"  # blue
co3 = "#000000"  # black
co4 = "#ff00ff"  # light purple

mixer.init()

window = Tk()
window.title("Music Player")
window.geometry('352x255')
window.configure(background=co1)
window.resizable(width=False, height=False)

songs = 0
index = 0

# function for open folder


def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                listbox.insert(END, song)

# function for play_music


def play_music():
    try:
        paused
    except NameError:
        try:
            running = listbox.get(ACTIVE)
            running_song['text'] = running
            mixer.music.load(running)
            mixer.music.play()
            get_time()
        except:
            pass
    else:
        mixer.music.unpause()


# function for pause music


def pause_music():
    global paused
    paused = True
    mixer.music.pause()

# function for resume music


def continue_music():
    mixer.music.unpause()

# function for stop music


def rewind_music():
    # mixer.music.stop()
    # listbox.select_clear("active")
    play_music()

# function for next music


def next_music():
    next_song = listbox.curselection()
    next_song = next_song[0]+1
    next_song_name = listbox.get(next_song)
    running_song['text'] = next_song_name
    mixer.music.load(next_song_name)
    mixer.music.play()
    listbox.select_clear(0, 'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

# function for previous music


def previous_music():
    prev_song = listbox.curselection()
    prev_song = prev_song[0]-1
    prev_song_name = listbox.get(prev_song)
    running_song['text'] = prev_song_name
    mixer.music.load(prev_song_name)
    mixer.music.play()
    listbox.select_clear(0, 'end')
    listbox.activate(prev_song)
    listbox.select_set(prev_song)

# function for mute song


def mute():
    scale.set(0)
    unmute_button = Button(down_frame, image=img_mute, width=35, height=35,
                           padx=10, command=unmute, bd=0, font=("Ivy 10"))
    unmute_button.place(x=215+28, y=45)
    # running_song['text'] = 'Music_mute'
    # continue_music()
    running = listbox.get(ACTIVE)
    running_song['text'] = running

# function for unmute song


def unmute():
    scale.set(45)
    unmute_button = Button(down_frame, image=img_unmute, width=35, height=35,
                           padx=10, bd=0, font=("Ivy 10"), command=mute)
    unmute_button.place(x=215+28, y=45)
    # running_song['text'] = 'Music_unmute'
    # continue_music()
    running = listbox.get(ACTIVE)
    running_song['text'] = running

# function for volume bar


def volume(vol):
    volume = int(vol)/100
    mixer.music.set_volume(volume)

# function for music time


def get_time():
    current_time = mixer.music.get_pos()/1000
    formated_time = time.strftime("%H:%M:%S", time.gmtime(current_time))
    next_one = listbox.curselection()
    song = listbox.get(next_one)
    song_timer = MP3(song)
    song_length = int(song_timer.info.length)
    format_for_length = time.strftime("%H:%M:%S", time.gmtime(song_length))
    label_time.config(text=f"{format_for_length}/{formated_time}")
    progress["maximum"] = song_length
    progress["value"] = int(current_time)
    window.after(100, get_time)

# function for exit application


def exit_application():
    msg_box = messagebox.askquestion(
        'Exit Application', 'Are you sure you want to exit the application?')
    if msg_box == 'yes':
        window.destroy()
    else:
        messagebox.showinfo(
            'Return', 'you will now return to the application screen')


def About():
    messagebox.showinfo('About us', 'This is GUI based Music Player Created By Saddam Hussain,that allows you to listen to music files stored in the phone internal or external memory.an art of sound in time that expresses ideas and emotions in significant forms through the elements of rhythm, melody, harmony, and color. the tones or sounds employed, occurring in single line (melody) or multiple lines (harmony), and sounded or to be sounded by one or more voices or instruments, or both.')


# all frame
left_frame = Frame(window, width=150, height=150, bg=co1)
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = Frame(window, width=250, height=150, bg=co3)
right_frame.grid(row=0, column=1, padx=0)

down_frame = Frame(window, width=400, height=100, bg=co4)
down_frame.grid(row=1, column=0, columnspan=3, padx=0, pady=1)
# list of song
listbox = Listbox(right_frame, font=("Arial", 10), width=22, bd=0)
# scrolling song
scroll = Scrollbar(right_frame, bg=co1)
listbox.config(yscrollcommand=scroll.set, bg=co3, fg=co1,
               selectbackground="lightblue", cursor="hand2")
scroll.config(command=listbox.yview)
scroll.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH)

# image icon
img_1 = Image.open("9.png")
img_1 = img_1.resize((130, 130))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, height=130, image=img_1, padx=10, bg=co1)
app_image.place(x=10, y=15)

img_2 = Image.open("4.png")
img_2 = img_2.resize((30, 30))
img_2 = ImageTk.PhotoImage(img_2)
play_button = Button(down_frame, width=35, height=35, image=img_2,
                     padx=10, bg=co1, font=("Ivy 10"), command=play_music)
play_button.place(x=10+28, y=45)

img_3 = Image.open("5.png")
img_3 = img_3.resize((30, 30))
img_3 = ImageTk.PhotoImage(img_3)
prev_button = Button(down_frame, width=35, height=35, image=img_3,
                     padx=10, bg=co1, font=("Ivy 10"), command=previous_music)
prev_button.place(x=0, y=45)

img_4 = Image.open("6.png")
img_4 = img_4.resize((30, 30))
img_4 = ImageTk.PhotoImage(img_4)
next_button = Button(down_frame, width=35, height=35, image=img_4,
                     padx=10, bg=co1, font=("Ivy 10"), command=next_music)
next_button.place(x=51+28, y=45)

img_5 = Image.open("1.png")
img_5 = img_5.resize((30, 30))
img_5 = ImageTk.PhotoImage(img_5)
pause_button = Button(down_frame, width=35, height=35, image=img_5,
                      padx=10, bg=co1, font=("Ivy 10"), command=pause_music)
pause_button.place(x=92+28, y=45)

img_6 = Image.open("3.png")
img_6 = img_6.resize((30, 30))
img_6 = ImageTk.PhotoImage(img_6)
continue_button = Button(down_frame, width=35, height=35, image=img_6,
                         padx=10, bg=co1, font=("Ivy 10"), command=continue_music)
continue_button.place(x=133+28, y=45)

img_7 = Image.open("2.png")
img_7 = img_7.resize((30, 30))
img_7 = ImageTk.PhotoImage(img_7)
rewind_button = Button(down_frame, width=35, height=35, image=img_7,
                       padx=10, bg=co1, font=("Ivy 10"), command=rewind_music)
rewind_button.place(x=174+28, y=45)

img_unmute = Image.open("unmute.png")
img_unmute = img_unmute.resize((30, 30))
img_unmute = ImageTk.PhotoImage(img_unmute)
img_mute = Image.open("mute.png")
img_mute = img_mute.resize((30, 30))
img_mute = ImageTk.PhotoImage(img_mute)
unmute_button = Button(down_frame, image=img_unmute, width=35, height=35,
                       padx=10, bd=0, font=("Ivy 10"), command=mute)
unmute_button.place(x=215+28, y=45)

# volume bar
scale = Scale(down_frame, from_=0, to=100, bg="#40C057", bd=0,
              orient=HORIZONTAL, length=66, command=volume)
scale.set(50)
scale.place(x=253+28, y=45)

line = Label(left_frame, width=200, height=1, padx=10, bg=co1)
line.place(x=0, y=3)

running_song = Label(down_frame, text="Choose a song", font=(
    "Ivy 10"), width=44, height=1, padx=10, bg="black", fg="white", anchor="center")
running_song.place(x=0, y=1)

# open_folder
# open_folders = Button(window, text="Open Folder", width=10, height=0, font=("arial", 8, "bold"), fg="white", bg="black", command=open_folder)
# open_folders.place(x=0, y=1)

# progres bar
progress = ttk.Progressbar(
    down_frame, orient=HORIZONTAL, value=0, length=250, mode='determinate')
progress.place(x=0, y=23)
# time length
label_time = Label(down_frame, text="00:00:00/00:00:00",
                   font="Ivy 8", bg="#40C057", fg="white", width=16, height=1)
label_time.place(x=251, y=23)

# menu
menubar = Menu(window)
window.configure(menu=menubar)

submenu1 = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=submenu1)
submenu1.add_command(label='Open File', command=open_folder)
submenu1.add_command(label='Exit', command=exit_application)

submenu3 = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=submenu3)
submenu3.add_command(label='About', command=About)

music_state = StringVar()
music_state.set("Choose one!")
window.mainloop()
