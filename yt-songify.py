#!/usr/bin/python3

import sys
from subprocess import call
import youtube_dl
from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE2, TPE1, TCON, TDRC

dl_options = {
    "outtmpl": "%(id)s.%(ext)s",
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }]
}

with youtube_dl.YoutubeDL(dl_options) as dl:
    dl.download([sys.argv[1]])
    filename = dl.extract_info(sys.argv[1], download = False)["id"] + ".mp3"

metadata = {}
metadata["title"] = str(input("Song Title: "))
metadata["album"] = str(input("Album Name: "))
metadata["artist"] = str(input("Artist Name: "))
metadata["genre"] = str(input("Genre: "))
metadata["year"] = str(input("Year: "))

audio = ID3(filename)
audio.add(TIT2(encoding = 3, text = metadata["title"]))
audio.add(TALB(encoding = 3, text = metadata["album"]))
audio.add(TPE2(encoding = 3, text = metadata["artist"]))
audio.add(TPE1(encoding = 3, text = metadata["artist"]))
audio.add(TCON(encoding = 3, text = metadata["genre"]))
audio.add(TDRC(encoding = 3, text = metadata["year"]))
audio.save()