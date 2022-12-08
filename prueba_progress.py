import eyed3
import os
import shutil
from utils.file_loader import (
    filename_database,
    folder_creator,
    printProgressBar,
    name_cleaning,
)
import re

#   Documentación importante
# https://eyed3.readthedocs.io/en/latest/eyed3.id3.html#module-eyed3.id3.tag

cwd, lista = filename_database()
new_folder = f"{cwd}\\Music_library"
l = len(lista)

printProgressBar(0, l, prefix="Progress:", suffix="Complete", length=50)

# for element in lista:
#     print(element)
# raise SystemExit
try:
    os.makedirs(new_folder)
except FileExistsError:
    print("Ya existe una carpeta con este Nombre.")
    shutil.rmtree(new_folder)
    os.makedirs(new_folder)

    # raise SystemExit
pattern = r"[\[\]\\\/\:\<\>\*\?\"\-\|]+"
pattern2 = r"\(.*?\)"
pattern3 = r"\[.*?\]"
for i, filename in enumerate(lista):
    file_path = f"{cwd}\\{filename}"
    audiofile = eyed3.load(file_path)
    # print(f"Procesando: {audiofile.tag.title}")

    album = audiofile.tag.album
    artist = audiofile.tag.artist
    title = audiofile.tag.title
    if album == None:
        album = "Unkown Album"
    if artist == None:
        artist = "Unkown Artist"
    if title == None:
        title = f"Unkown Title {i}"

    # Para eliminar los caracteres que no pueden estar en el nombre
    # de la carpeta: [\/:<>*?"|]

    # album = re.sub(pattern, "", album)
    # album = re.sub(pattern3, "", album)
    # album = album.strip()
    # album = album.replace("...","")
    album = name_cleaning(album)
    # print(album)
    # artist = re.sub(pattern, "", artist)
    # artist = artist.strip()
    artist = name_cleaning(artist)
    artis_dir_name = f"{new_folder}\\{artist}"
    album_dir_name = f"{new_folder}\\{artist}\\{album}"

    folder_creator(artis_dir_name)
    folder_creator(album_dir_name)
    # new_file_name = f"{artist} - {title} - {album}"
    new_file_name = f"{artist} - {title}"
    # new_file_name = re.sub(pattern2, "", new_file_name)
    # new_file_name = re.sub(pattern, "", new_file_name)
    new_file_name = name_cleaning(new_file_name)
    # title = re.sub(pattern, "", title)

    # title = re.sub(pattern2, "", title)
    title = name_cleaning(title)
    # title = re.sub(pattern3, "", title)
    new_file_path = f"{new_folder}\\{artist}\\{album}\\{new_file_name}.mp3"
    # print(new_file_name)
    shutil.copy2(file_path, new_file_path)
    printProgressBar(i + 1, l, prefix="Progress:", suffix="Complete", length=50)

    # print(f"Procesando: {new_file_name}")

# audiofile = eyed3.load("C:\\Users\\USER\\Documents\\Alvaro\\prueba_musica\\Musica\\1-07 Heroin.mp3")
# # audiofile = eyed3.core.load("C:\\Users\\USER\\Documents\\Alvaro\\prueba_musica\\Musica\\1-07 Heroin.mp3")
# print(audiofile.tag.title)
# print(audiofile.tag.artist)
# print(audiofile.tag.album)
# print(audiofile.tag.album_artist)
# print(audiofile.tag.composer)
# print(audiofile.tag.publisher)
# print(audiofile.tag.genre.name)
# print(audiofile.tag.recording_date)
# print(audiofile.tag.publisher)
# print(audiofile.tag.cd_id)
