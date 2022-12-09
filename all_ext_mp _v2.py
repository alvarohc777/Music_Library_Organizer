# Para leer metadatos

import eyed3
import time

# Para navegar por los directorios
import os

# Para copiar y mover archivos
import shutil

# Para correr el código en paralelo

import concurrent.futures
from itertools import repeat

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
    parallel_iter2,
)


def main():

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
    cores = os.cpu_count()
    exts = [".m4a", ".flac"]
    listas = [list_mp4, list_flac]
    t0 = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=cores - 1) as executor:
        executor.map(parallel_iter2, listas, repeat(cwd), repeat(new_folder), exts)
    tf = time.perf_counter()
    print(f"Tiempo del script {tf-t0}s")
    # Archivos: 166
    # Tiempo del script 242.29163759999938s


if __name__ == "__main__":
    main()
