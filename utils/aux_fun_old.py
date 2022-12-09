import pickle
import glob
import os
from mutagen.mp3 import MP3


def no_metadata_exception(file_path, title=None, album=None, artist=None):
    basename = os.path.basename(file_path)
    root, _ = os.path.splitext(basename)
    album = "unkown album"
    artist = "unkown artist"
    return title, album, artist


lista = glob.glob(r"**/*.mp3", recursive=True)
print(len(lista))
cwd = os.getcwd()
lista_canciones = []
for file in lista:
    audiofile = MP3(f"{cwd}\\{file}")
    try:
        title = audiofile["TIT2"].text[0]
        artist = audiofile["TPE1"].text[0]
        title = f"{artist} - {title}"
    except KeyError:
        title, *_ = no_metadata_exception(f"{cwd}\\{file}")
        if title == None:
            print(file)
    lista_canciones.append(title)


with open("lista_canciones_viejas", "wb") as f:
    pickle.dump(lista_canciones, f)
