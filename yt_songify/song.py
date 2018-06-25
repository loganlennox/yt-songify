import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TALB, TPE2, TPE1, TCON, TDRC

class Song:
    def __init__(self, filename):
        self.filename = filename
        self.music = ID3(self.filename)

    def add_name(self, data):
        self.music.add(TIT2(encoding = 3, text = data))
        self.music.save()

    def add_artist(self, data):
        self.music = ID3(self.filename)
        self.music.add(TPE1(encoding = 3, text = data))
        self.music.save()

    def add_band(self, data):
        self.music.add(TPE2(encoding = 3, text = data))
        self.music.save()

    def add_album(self, data):
        self.music.add(TALB(encoding = 3, text = data))
        self.music.save()

    def add_genre(self, data):
        self.music.add(TCON(encoding = 3, text = data))
        self.music.save()

    def add_year(self, data):
        self.music.add(TDRC(encoding = 3, text = data))
        self.music.save()

    def add_coverart(self, filename, description):
        with open(filename, "rb") as coverart:
            self.music.add(APIC(
                encoding = 3,
                mime = "image/png",
                type = 3,
                desc = description,
                data = coverart.read()
            ))
        self.music.save()

    def set_filename(self, filename):
        filename = filename + ".mp3"
        os.rename(self.filename, filename)
        self.filename = filename
