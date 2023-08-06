import os
from zipfile import  ZipFile
from pathlib import Path
from shutil import move, copy2


def is_directory(path):
    return Path(path).is_dir()


def get_files(directory, filters="*"):
    if Path(directory).exists() and is_directory(directory):
        files = Path(directory).glob(filters)
        for file in files:
            yield file
    else:
        return


def unzip_folder(zip_folder_path, target_folder=os.getcwd()):
    zip_file = ZipFile(zip_folder_path, 'r')
    zip_file.extractall(target_folder)
    zip_file.close()


def unzip_folders(zip_folder_path, target_folder=os.getcwd()):
    zipfiles = get_files(zip_folder_path, "**/*.zip")
    for file_item in zipfiles:
        unzip_folder(file_item)


def copy_file(sourcefolder, targetfolder=os.getcwd()):
    if(is_directory(sourcefolder)):
        copy2(sourcefolder, targetfolder)

def copy_files(sourcefolder, targetfolder=os.getcwd(), filters="*"):
    if(is_directory(sourcefolder)):
        files = get_files(sourcefolder, filters)
        for file_item in files:
            copy2(file_item, targetfolder)


def move_file(source, target=os.getcwd()):
    if(is_directory(source)):
            move(source, target)

def move_files(sourcefolder, targetfolder=os.getcwd(), filters="*"):
    if(is_directory(sourcefolder)):
        files = get_files(sourcefolder, filters)
        for file_item in files:
            move(file_item, targetfolder)

