import os
import shutil


def delete_path(path):
    if os.path.exists(path):
        shutil.rmtree(path)


def create_folder(path):
    if os._exists(path):
        shutil.rmtree(path)
