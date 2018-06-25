import youtube_dl

def download_file(url):
    options = {
        "outtmpl": "%(id)s.%(ext)s",
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    }

    with youtube_dl.YoutubeDL(options) as dl:
        dl.download([url])
        return dl.extract_info(url, download = False)["id"] + ".mp3"
