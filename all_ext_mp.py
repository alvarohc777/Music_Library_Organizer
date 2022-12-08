# Para leer metadatos

import eyed3
import time

# Para navegar por los directorios
import os

# Para copiar y mover archivos
import shutil

from utils.file_loader import (
    database_mp3,
    database_mp4,
    database_flac,
    metadata_mp3,
    metadata_mp4,
    metadata_flac,
    folder_creator,
    printProgressBar,
    name_cleaning,
    name_creator,
)


cwd = os.getcwd()
print(cwd)
new_folder = f"{cwd}\\Music_library"

try:
    os.mkdir(new_folder)
except:
    print("Ya existe una carpeta con este nombre.")
    # Por fines del development borro la carpeta si ya existe
    # debo quitar esto en producción.
    shutil.rmtree(new_folder)
    os.mkdir(new_folder)


list_mp3 = database_mp3()
list_mp4 = database_mp4()
list_flac = database_flac()
# l = len()
print(len(list_mp3))

# Inicializa la barra de progreso
# printProgressBar(0, l, prefix="Progress:", suffix="Complete", length=50)

# for i, filename in enumerate(list_mp3):
#     file_path = f"{cwd}\\{filename}"
#     title, artist, album = metadata_mp3(file_path)

#     print(title)

t0 = time.perf_counter()
for i, filename in enumerate(list_flac):
    file_path = f"{cwd}\\{filename}"
    title, artist, album = metadata_flac(file_path)
    new_file_name = name_creator(title, artist, album, new_folder)
    new_file_path = f"{new_folder}\\{artist}\\{album}\\{new_file_name}.flac"
    shutil.copy2(file_path, new_file_path)
    print(title, i)
tf = time.perf_counter()
print(f"Tiempo del script {tf-t0}s")

# for i, filename in enumerate(list_mp4):
#     file_path = f"{cwd}\\{filename}"
#     title, artist, album = metadata_mp4(file_path)
#     new_file_name = name_creator(title, artist, album, new_folder)
#     new_file_path = f"{new_folder}\\{artist}\\{album}\\{new_file_name}.m4a"
#     shutil.copy2(file_path, new_file_path)

#     print(title, i)

# for i, filename in enumerate(list_mp3):
#     file_path = f"{cwd}\\{filename}"
#     title, artist, album = metadata_mp3(file_path)
#     new_file_name = name_creator(title, artist, album, new_folder)
#     new_file_path = f"{new_folder}\\{artist}\\{album}\\{new_file_name}.mp3"
#     if len(new_file_path) > 256:
#         new_file_path = f"{new_file_path[:251]}.mp3"
#     shutil.copy2(file_path, new_file_path)

#     print(title, i)
