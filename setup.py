from setuptools import setup

setup(name = "yt-songify",
      version = "0.1",
      description = "Command-line tool that downloads content from YouTube as mp3 files and adds proper metadata.",
      url = "https://github.com/loganlennox/yt-songify",
      author = "Logan Lennox",
      author_email = "loganlennox@protonmail.com",
      license = "MIT",
      packages = ["yt-songify"],
      scripts = ["bin/yt-songify"],
      include_package_data = True,
      install_requires = [
          "youtube-dl",
          "mutagen",
      ],
      zip_safe = False)
