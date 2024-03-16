
import logging
import os
from pathlib import Path
from collections import namedtuple
import argparse


DirObject = namedtuple(
    'DirObject', ['name_file', 'extension_file', 'file_folder', 'root'], defaults=['', '', '', ''])

logging.basicConfig(filename='dir_objects.log.', filemode='w',
                    encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def folder_info(dir_path: str | Path = None):
    if dir_path is None:
        dir_path = Path(os.getcwd())
    objects_list = []

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            name_ = Path(file).stem
            n, extension_ = os.path.splitext(file)
            root_name, dir_ = os.path.split(root)
            file_info = DirObject(name_, extension_,  dir_, root_name)
            objects_list.append(file_info)
            logger.info(file_info)

    return objects_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Enter file path.')
    parser.add_argument('path', type=str, default=Path(__file__).parent)

    arg = parser.parse_args()

    print(folder_info(Path(arg.path)))
    # folder_info()
