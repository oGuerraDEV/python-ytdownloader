from pytubefix import YouTube, Playlist
import os
import re

filetype = input("Baixar audio ou video: (1 - Audio 2- Video): ")
link = input("Link: ")

playlist = Playlist(link)

videoamout = len(playlist.videos)

print("Nome da playlist: ", playlist.title)
print("Numero de videos: ", videoamout)

for url in playlist:
    video = YouTube(url)
    if filetype == "1":
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename_prefix=playlist.title+" - ", output_path='playlists')
    elif filetype == "2":
        resolution = input("Escolha a resolucao de download: (2160p, 1080p, 720p, 480p, 360p, 240p, 144p): "
                   "Caso o video nao tenha a resolucao selecionada, o download falhara: "
                   )
        stream = video.streams.filter(res=str(resolution)).first()
        stream.download(output_path='playlists')