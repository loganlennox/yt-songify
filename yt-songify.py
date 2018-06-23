#!/usr/bin/python3

import sys
from subprocess import call
import youtube_dl

dl_url = sys.argv[1]

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
    dl.download([dl_url])