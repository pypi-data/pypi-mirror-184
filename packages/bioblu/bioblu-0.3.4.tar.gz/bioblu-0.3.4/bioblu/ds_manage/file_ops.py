import json
import logging
import os
import shutil
from pathlib import Path
from typing import Tuple, List

import cv2
import numpy as np


def all_x_have_y(fdir: str, ext_x: str, ext_y: str, recursive=True) -> bool:
    """
    ToDo: Think about how to do this with multiple x and y extensions.
    Checks if all files (in folder fdir) with the extension ext_x have a corresponding file with the extension ext_y.
    :param fdir:
    :param ext_x:
    :param ext_y:
    :param recursive:
    :return:
    """
    x_fpaths = get_all_fpaths_by_extension(fdir, (ext_x,), recursive=recursive)
    y_fpaths = get_all_fpaths_by_extension(fdir, (ext_y,), recursive=recursive)

    results = []
    for xpath in x_fpaths:
        basename_x = os.path.splitext(os.path.split(xpath)[-1])[0]
        found_match = False
        for ypath in y_fpaths:
            basename_y = os.path.splitext(os.path.split(ypath)[-1])[0]
            if basename_x == basename_y:
                found_match = True
                break
        if not found_match:
            print(f"No match for file: {xpath}")
        results.append(found_match)
    return all(results)


def get_corresponding_file(base_file: str, checkdir: str, extensions: Tuple[str]) -> str:
    """
    Checks against files in checkdir if there is a file corresponding to the file specified as fpath_file.
    Can include or exclude extension. \n
    :param base_file: path or filename
    :param checkdir: fdir
    :param keep_extension: bool
    :param extension:
    :return:
    """
    extensions = tuple(ext.lower() for ext in extensions)

    basename = os.path.split(base_file)[-1].rsplit(".")[0]
    matches = []
    for root, dirs, files in os.walk(checkdir):
        for file in files:
            if file.lower().endswith(extensions):
                file_basename = file.rsplit(".")[0]
                if file_basename == basename:
                    matches.append(os.path.join(root, file))
    if not matches:
        return None
    if len(matches) > 1:
        print(f"More than one match found:\n{matches}")
        return matches
    return matches[0]


def get_file_pairs(fdir, ext_1, ext_2, recursive=False) -> List[tuple]:

    fpaths_0 = get_all_fpaths_by_extension(fdir, ext_1, recursive=recursive)
    fpaths_1 = get_all_fpaths_by_extension(fdir, ext_2, recursive=recursive)

    basenames_0 = [os.path.splitext(os.path.basename(f))[0] for f in fpaths_0]
    basenames_1 = [os.path.splitext(os.path.basename(f))[0] for f in fpaths_1]

    # Outcommented bc. differing length does not necessarily mean duplicates. It can also mean e.g. fewer txt files than imgs.
    # if len(fpaths_0) != len(set(fpaths_0)):
    #     raise FileExistsError(f"There are duplicates among the {ext_1} files.")
    # if len(fpaths_1) != len(set(fpaths_1)):
    #     raise FileExistsError(f"There are duplicates among the {ext_2} files.")
    # if len(basenames_0) == len(set(basenames_0)):
    #     print("Duplicates by name (w/o ext) in first group.")
    # if len(basenames_1) == len(set(basenames_1)):
    #     print("Duplicates by name (w/o ext) in second group.")

    file_pairs = []
    for fpath_0 in fpaths_0:
        basename_0 = os.path.basename(fpath_0)
        paired_element_index = None
        # logging.debug(f"Length of lookup list: {len(fpaths_1)}")
        for i, fpath_1 in enumerate(fpaths_1):
            basename_1 = os.path.basename(fpath_1)
            if basename_0.split(".")[0] == basename_1.split(".")[0]:
                file_pairs.append((fpath_0, fpath_1))
                paired_element_index = i
                break
        if paired_element_index is not None:
            fpaths_1.pop(paired_element_index)
    return file_pairs


def is_empty(fdir) -> bool:
    return not os.listdir(fdir)


def get_basename_only(fpath) -> str:
    """
    Strips off the path and the file extension.
    :param fpath:
    :return:
    """
    fname = os.path.split(fpath)[-1]
    fname = os.path.splitext(fname)[0]
    return fname


def images_are_identical(fpath_img_1, fpath_img_2) -> bool:
    img_1 = cv2.imread(fpath_img_1)
    img_2 = cv2.imread(fpath_img_2)
    return np.all(img_1 == img_2)


def get_all_fpaths_by_extension(root_fdir: str, exts: Tuple[str, ...], recursive=True) -> List[str]:
    """
    Recursively extracts all file paths to files ending with the given extension down the folder hierarchy (i.e. it
    includes subfolders).
    :param root_fdir: str. Root directory from where to start searching
    :param exts: Tuple of extension strings. e.g. (".txt", "WAV")
    :param recursive:
    :return: sorted list of file paths
    """
    logging.debug(exts)
    exts = (ext.lower() for ext in exts)
    # Make sure they have a preceding period
    exts = tuple([ext if ext.startswith(".") else "." + ext for ext in exts])
    if recursive:
        file_paths = [str(path) for path in Path(root_fdir).rglob('*') if path.suffix.lower() in exts]
    else:
        file_paths = [os.path.join(root_fdir, fname) for fname in sorted(os.listdir(root_fdir)) if fname.endswith(exts)]
    return sorted(file_paths)


def add_file_prefix(fdir, prefix) -> None:
    """Adds the prefix to all files in the given directory"""
    fpaths = [os.path.join(fdir, fname) for fname in os.listdir(fdir)]
    assert all([os.path.isfile(p) for p in fpaths])
    for fpath in fpaths:
        old_name = os.path.basename(fpath)
        new_name = f"{prefix}{old_name}"
        src = fpath
        dst = os.path.join(fdir, new_name)
        assert not os.path.isfile(dst)
        shutil.move(src, dst)


def get_paths_to_txt_files(fdir, recursive=True) -> List[str]:
    """
    Returns a list of the paths to all annotation files in the dataset (assumes a yolo-structured dataset).
    :param fdir: Base dir of a yolo dataset.
    :param recursive:
    :return: list of paths
    """
    return get_all_fpaths_by_extension(fdir, ("txt",), recursive=recursive)


def load_json(json_fpath: str) -> dict:
    """Returns json data as a dict."""
    with open(json_fpath, 'r') as f:
        data = json.load(f)
    # logging.debug(f'Loaded json object (type): {type(data)}')
    return data
