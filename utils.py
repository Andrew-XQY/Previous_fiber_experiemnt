import os
import numpy as np
from PIL import Image
from typing import *


def image_splitter(narray_img) -> Tuple[np.array, np.array]:
    return np.array_split(narray_img, 2, axis=1)


def get_all_file_paths(dir:str, types=['']) -> list:
    file_paths = []  # List to store file paths
    for root, _, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(os.path.abspath(file_path))
    return [file for file in file_paths if any(type in file for type in types)]


def get_all_images(dir:str) -> list:
    paths = get_all_file_paths(dir)
    return [Image.open(i) for i in paths]


def get_all_images_as_nparray(dir:str) -> list:
    return [np.array(i) for i in get_all_images(dir)]





