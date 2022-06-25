from tkinter import *
from tkinter.ttk import Progressbar
import pytube
import os
from pathlib import Path
import time
from tkinter import ttk


downloads_path = str(Path.home() / "Downloads")
#keydown
def click():
    link=textentry.get()
    output.delete(0.0, END)
    try:   
        yt = pytube.YouTube(link)
        ys = yt.streams.get_highest_resolution()
        text = "Dowloading"
        ys.download(downloads_path)
        text = "Dowloaded"
    except:     
        text = "Not a vaild link"
    output.insert(END, text)
#main
window = Tk()
window.title("Youtube_video_downloader")
window.configure(background="#2e2c35")

#center
window_width = 300
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
window.geometry(f'{window_height}x{window_width}+{center_x}+{center_y}')

Label(window, text="Enter link bellow", bg ="#2e2c35", fg="White", font= "arial 24 bold",).pack(pady=10, padx=10)
#Text Entry box
textentry = Entry(window, width=22, bg="white", font="ariall 24 bold")
textentry.pack(pady=10, padx=10)
#dowload button

Button(window, text="Dowload", width = 56, command=click).pack(pady=10, padx=10)
#progressbar (not functiong)
'''pb = Progressbar(window, orient="horizontal", length=250, mode="determinate")
pb.grid(row = 4, column = 0)'''

#output
output = Text(window, width=44, height=2, wrap=WORD, background="#2e2c35", fg="White", font="arial 12 bold")
output.pack(pady=10, padx=10)

#mainloop for gui
window.mainloop()