
from pytube import YouTube
from tkinter import *
link = input("link: ")
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
ys.download()