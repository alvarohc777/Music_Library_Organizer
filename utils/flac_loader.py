from mutagen.flac import FLAC
from mutagen.mp4 import MP4
from mutagen.mp3 import MP3

PATH = "C:\\Users\\USER\\Documents\\Alvaro\\prueba_musica\\Music\\Radiohead Complete Studio Discography [FLAC]\\Radiohead - 2011 - The King of Limbs\\05 - Lotus Flower.flac"
audiofile = FLAC(PATH)

title = audiofile["title"][0]
album = audiofile["album"][0]
artist = audiofile["artist"][0]
# Acceder a este como si fuera un diccionario

PATH = "C:\\Users\\USER\\Documents\\Alvaro\\prueba_musica\\Music\\Radiohead Complete Studio Discography [FLAC]\\Radiohead - 2011 - The King of Limbs\\05 - Lotus Flower.m4a"
audiofile = MP4(PATH)
title = audiofile["\xa9nam"]
album = audiofile["\xa9alb"]
artist = audiofile["\xa9ART"]

# MP3
# 'C:\\Users\\USER\\Documents\\Alvaro\\prueba_musica\\Music\\†\\Justice - 06 - Phantom Pt II.mp3'
audiofile = MP3(PATH)
title = audiofile["TIT2"].text[0]
album = audiofile["TALB"].text[0]
artist = audiofile["TPE1"].text[0]
