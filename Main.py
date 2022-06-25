from tkinter import *
from turtle import window_width
import pytube
from pyparsing import White

#keydown
def click():
    link=textentry.get()
    output.delete(0.0, END)
    try:   
        yt = pytube.YouTube(link)
        ys = yt.streams.get_highest_resolution()
        ys.download()
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

Label(window, text="Enter link bellow", bg ="#2e2c35", fg="White", font= "arial 24 bold",).grid(row=0, column=0, stick=W)
#Text Entry box
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=1, column=0, sticky=W)
#dowload button

Button(window, text="Dowload", width = 0, command=click) .grid(row=3, column=0, stick=W)
#output

output = Text(window, width=20, height=1, wrap=WORD, background="#2e2c35", fg="White", font="arial 12 bold")
output.grid(row=4, column=0, sticky=W)

#mainloop for gui
window.mainloop()