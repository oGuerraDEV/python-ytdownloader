from pytubefix import YouTube
from moviepy.editor import *
import os

link = input("Link: ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)
print("Author: ", yt.author)

yd = yt.streams.filter(only_audio=True).first()

download = input("Confirm download? (Y or N): ")

if download == "y" or "Y": 
    yd.download(output_path='output', filename="download.mp3") 
else:
    print("Download Cancelado")
