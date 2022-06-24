from tkinter import *
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
window.geometry("750x500+400+300")
Label(window, text="Enter link bellow", bg ="#2e2c35", fg="White", font= "arial 12 bold").grid(row=0, column=0, stick=W)
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=1, column=0, sticky=W)
Button(window, text="Dowload", width = 0, command=click) .grid(row=3, column=0, stick=W)
output = Text(window, width=20, height=1, wrap=WORD, background="#2e2c35", fg="White", font="arial 12 bold")
output.grid(row=4, column=0, sticky=W)


window.mainloop()