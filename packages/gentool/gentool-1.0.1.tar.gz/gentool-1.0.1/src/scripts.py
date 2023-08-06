"""General helper functions.
"""
import os
from zipfile import  ZipFile
from pathlib import Path
import shutil

from src.utils.chmod import *


def is_directory(path):
    """Checks if path is a directory.
    Parameters:
        path (str): The path to test
    Returns:
        bool : true if path is a directory or false if not.
    """
    return Path(os.path.normpath(path)).is_dir()


def get_files(directory, filters="**/"):
    """ Grab Files in a specified path.
    
    Parameters:
        directory (str): The directory to grab files from
        filters (str)all : specify the types of files to grab. wildcards accepted
        (default will grab everything)
    Returns:
        all the files in directory as a generator. if the path is  not a valid directory
        None will be returned
    """
    if Path(directory).exists() and is_directory(directory):
        files = Path(directory).glob(filters)
        for file in files:
            yield file
    else:
        return None


def unzip_folder(zip_folder_path, target_folder=os.getcwd()):
    zip_file = ZipFile(zip_folder_path, 'r')
    zip_file.extractall(target_folder)
    zip_file.close()

def unzip_folders(zip_folder_path, target_folder=os.getcwd()):
    zipfiles = get_files(zip_folder_path, "**/*.zip")
    for file_item in zipfiles:
        unzip_folder(file_item)


def copy_file(source, target=os.getcwd()):
    if(is_directory(source)):
        shutil.copy(source, target)

def copy_files(source, target=os.getcwd(), filters="**/"):

    if(is_directory(source)):
        print("starting")
        files = get_files(source, filters)
        for file_item in files:
            shutil.copy(file_item, target)


def move_file(source, target=os.getcwd()):
    if(is_directory(source)):
            shutil.move(source, target)

def move_files(source, target=os.getcwd(), filters="**/"):
    if(is_directory(source)):
        files = get_files(source, filters)
        for file_item in files:
            shutil.move(file_item, target)

#if __name__ == "__main__":
    #print(is_directory("tests/mocks"))
    #move_files('tests/mocks/t1',  'tests/mocks/a2')
