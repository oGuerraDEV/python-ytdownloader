from pytubefix import YouTube

link = input("Link: ")
#resolution = input("Escolha a resolucao de download: (2160p, 1080p, 720p, 480p, 360p, 240p, 144p): ")
yt = YouTube(link)

print("Title: ", yt.title)

print("Views: ", yt.views)
confirmd = input("Confirm the download (Y or N): ")

if confirmd == "y":
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path='output')
else:
    print("Download Cancelado")