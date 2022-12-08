import os
import glob
import shutil
import re

"""
Módulo utilizado para poder encontrar las carpetas y
archivos que contienen los archivos .mp3
"""


def filename_database():
    database_list = glob.glob(r"**/*.mp3", recursive=True)
    database_list2 = glob.glob(r"**/*.m4a", recursive=True)
    database_list = database_list + database_list2
    database_list3 = glob.glob(r"**/*.flac", recursive=True)
    database_list = database_list + database_list3
    cwd_path = os.getcwd()

    # print(len(database_list))
    # for file in database_list:
    #     print(f"{cwd_path}\\{file}")
    return cwd_path, database_list


def folder_creator(new_folder):
    try:
        os.makedirs(new_folder)
    except FileExistsError:
        # print("Ya existe")
        return


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


def main():
    database_list = glob.glob(r"**/*.mp3", recursive=True)
    print(database_list)


if __name__ == "__main__":
    main()
