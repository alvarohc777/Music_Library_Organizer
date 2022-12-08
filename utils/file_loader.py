import os
import glob
import shutil
import re
import eyed3

from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.flac import FLAC

"""
Módulo utilizado para poder encontrar las carpetas y
archivos que contienen los archivos .mp3
"""


def database_mp3():
    lista = glob.glob(r"**/*.mp3", recursive=True)
    return lista


def database_mp4():
    return glob.glob(r"**/*.m4a", recursive=True)


def database_flac():
    lista = glob.glob(r"**/*.flac", recursive=True)
    return lista


def metadata_mp4(file_path):
    audiofile = MP4(file_path)
    try:
        title = audiofile["\xa9nam"][0]
        album = audiofile["\xa9alb"][0]
        artist = audiofile["\xa9ART"][0]
        title = name_cleaning(title)
        album = name_cleaning(album)
        artist = name_cleaning(artist)
    except KeyError:
        title, album, artist = no_metadata_exception(file_path)

    return title, artist, album


def metadata_flac(file_path):
    audiofile = FLAC(file_path)
    try:
        title = audiofile["title"][0]
        album = audiofile["album"][0]
        artist = audiofile["artist"][0]
        title = name_cleaning(title)
        album = name_cleaning(album)
        artist = name_cleaning(artist)
    except KeyError:
        title, album, artist = no_metadata_exception(file_path)

    return title, artist, album


def metadata_mp3(file_path):
    audiofile = eyed3.load(file_path)

    album = audiofile.tag.album
    artist = audiofile.tag.artist
    title = audiofile.tag.title
    try:
        title = name_cleaning(title)
        album = name_cleaning(album)
        artist = name_cleaning(artist)
    except TypeError:
        title, album, artist = no_metadata_exception(file_path, title, album, artist)

    return title, artist, album


def no_metadata_exception(file_path, title=None, album=None, artist=None):
    basename = os.path.basename(file_path)
    root, _ = os.path.splitext(basename)
    title = name_cleaning(root)
    album = "unkown album"
    artist = "unkown artist"
    return title, album, artist


def folder_creator(new_folder):
    try:
        os.makedirs(new_folder)
    except FileExistsError:
        # print("Ya existe")
        return


def name_creator(title, artist, album, new_folder):
    artis_dir_name = f"{new_folder}\\{artist}"
    album_dir_name = f"{new_folder}\\{artist}\\{album}"
    folder_creator(artis_dir_name)
    folder_creator(album_dir_name)
    new_file_name = f"{artist} - {title}"
    return new_file_name


# Print iterations progress
def printProgressBar(
    iteration,
    total,
    prefix="",
    suffix="",
    decimals=1,
    length=100,
    fill="█",
    printEnd="\r",
):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def name_cleaning(file):
    pattern = r"[\[\]\\\/\:\<\>\*\?\"\-\|]+"
    pattern_parentheses = r"\(.*?\)"
    pattern_brackets = r"\[.*?\]"
    pattern_whitespace = r" +"
    file = re.sub(pattern, "", file)
    file = re.sub(pattern_parentheses, "", file)
    file = re.sub(pattern_brackets, "", file)
    file = file.strip()
    file = file.replace("...", "")
    file = re.sub(pattern_whitespace, " ", file)
    return file


def data_iterator(list_mp3, list_mp4, list_flac):
    for i, filename in enumerate(list_mp3):
        file_path = f"{cwd}\\{filename}"
        title, artist, album = metadata_mp3(file_path)
        new_file_name = name_creator(title, artist, album, new_folder)
        new_file_path = f"{new_folder}\\{artist}\\{album}\\{new_file_name}.mp3"
        if len(new_file_path) > 256:
            new_file_path = f"{new_file_path[:251]}.mp3"
        shutil.copy2(file_path, new_file_path)

        print(title, i)

def main():
    database_list = glob.glob(r"**/*.mp3", recursive=True)
    print(database_list)


if __name__ == "__main__":
    main()
