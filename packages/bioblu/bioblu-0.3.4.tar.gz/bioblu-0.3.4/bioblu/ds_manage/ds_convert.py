#!/usr/bin/env python3
import sys

import cv2
import datetime
import json
import logging
import numpy as np
import os
import pandas as pd
from pathlib import Path
from PIL import Image, UnidentifiedImageError
import random
import shutil
import termcolor
import time
from typing import List, Tuple, Dict, Union

import bioblu.ds_manage as ds_manage
import bioblu.ds_manage.file_ops

from bioblu.ds_manage import ds_annotations
from bioblu.ds_manage import ds_split
from bioblu.ds_manage import bbox_conversions
from bioblu.ds_manage.bbox_conversions import BoxFormatError
from bioblu.yolo import yolo_tools

from detectron2.structures import BoxMode

from bioblu.main import YOLO_IMG_FORMATS, IMG_FORMATS


def is_valid_img(img_path) -> bool:
    try:
        img = Image.open(img_path)
    except UnidentifiedImageError:
        return False
    else:
        return True
    finally:
        img = []


def subfolders_exist(fdir) -> bool:
    _filelist = os.listdir(fdir)
    _subdirs = [elem for elem in _filelist if os.path.isdir(os.path.join(fdir, elem))]#
    return bool(_subdirs)  # Because empty lists equate to False.


def invert_dictionary(in_dict: dict) -> dict:
    """Inverts a dict (keys become values and vice versa)"""
    return {value: key for key, value in in_dict.items()}


def cvt_yolo_annotations_to_coco_json(fdir_label_txts: str, fdir_imgs: str, fpath_dst: str, materials_dict: dict,
                                      exist_ok=False):
    """
    UNTESTED!
    :param fdir_label_txts:
    :param fdir_imgs:
    :param fpath_dst:
    :param materials_dict:
    :param exist_ok:
    :return:
    """
    txt_files = bioblu.ds_manage.file_ops.get_all_fpaths_by_extension(fdir_label_txts, (".txt",))
    img_files = bioblu.ds_manage.file_ops.get_all_fpaths_by_extension(fdir_imgs, YOLO_IMG_FORMATS)

    material_categories = [{"id": key, "name": value, "supercategory": value} for key, value in materials_dict.items()]
    print(material_categories)

    json_file = {"info": {"year": format(datetime.datetime.now(), "%Y"),
                          "version": None,
                          "description": f"COCO-version of the yolo labels in {fdir_label_txts}",
                          "contributor": None,
                          "url": None,
                          "date_created": format(datetime.datetime.now(), "%Y-%m-%d")},
                 "licences": [{"id": None,
                               "url": None,
                               "name": None}],
                 "categories": None}
    if not exist_ok and os.path.isfile(fpath_dst):
        raise FileExistsError()
    else:
        with open(fpath_dst, "w") as f:
            f.write(json.dumps(json_file, indent=2))


def create_labelme_json_from_yolo(fpath_yolo_txt: str, fpath_img: str, materials_dict: dict,
                                  save_dir:  str = None, include_img_data=False, overwrite=False) -> None:
    """
    Note that the image is necessary to convert between absolute and relative box coordinates!
    :param fpath_yolo_txt:
    :param fpath_img:
    :param materials_dict:
    :param save_dir:
    :param include_img_data:
    :param overwrite:
    :return:
    """
    logging.debug(f"Mats dict: {materials_dict}")
    fdir, fname_yolo_txt = os.path.split(fpath_yolo_txt)
    fname_base_txt = bioblu.ds_manage.file_ops.get_basename_only(fpath_yolo_txt)
    fname_base_img = bioblu.ds_manage.file_ops.get_basename_only(fpath_img)
    if not fname_base_img == fname_base_txt:
        raise AssertionError(f"File mismatch: {fpath_yolo_txt} and {fpath_img}")

    bboxes = ds_annotations.load_yolo_annotations_as_BBoxes(fpath_annotations_txt=fpath_yolo_txt, img_fpath=fpath_img,
                                                            materials_dict=materials_dict)
    annotation = ds_annotations.LabelmeAnnotation(abs_img_fpath=fpath_img, annotations=bboxes,
                                                  save_img_data=include_img_data)
    if save_dir is None:
        save_dir = fdir
    json_target_path = os.path.join(save_dir, f"{fname_base_txt}.json")
    if len(annotation.shapes) > 0:
        annotation.to_json(fpath_dst=json_target_path, overwrite=overwrite)
        logging.info(f"Created json at: {json_target_path}")
    else:
        logging.info(f"No json file created for {fname_base_txt} because no labels.")


def create_labelme_jsons_from_all_yolo_txts(fdir_root, materials_dict, include_img_data=False, overwrite=False):
    """Recursively creates labelme jsons from yolo txts."""
    pairs = get_yolo_img_annotation_pairs(fdir_root)
    pair_count = len(pairs)
    for i, (fpath_img, fpath_txt) in enumerate(pairs, start=1):
        print(f"Processing pair {i}/{pair_count}")
        json_target = os.path.join(fpath_txt.rsplit('.')[0] + ".json")
        if os.path.exists(json_target) and not overwrite:
            print(f"Skipping existing file (or pass overwrite=True): {json_target}")
            continue
        create_labelme_json_from_yolo(fpath_txt, fpath_img, materials_dict=materials_dict,
                                      include_img_data=include_img_data, overwrite=overwrite)


def add_img_dims(img_df: pd.DataFrame, img_dir):
    img_widths, img_heights = [], []
    logging.info('Extracting image dimensions')
    for i, line in img_df.iterrows():
        img_path = os.path.join(img_dir, line['img_name'])
        height, width, _ = cv2.imread(img_path).shape
        img_widths.append(width)
        img_heights.append(height)
    img_df['img_width'] = img_widths
    img_df['img_height'] = img_heights
    return img_df


def add_set_column(annotations: pd.DataFrame, split_dict: dict, index_column_name = 'file_name') -> pd.DataFrame:
    # ToDo: refactor this into ds_split
    """Adds a column "set" to the annotations pd.df that has the values "train", "val" and "test", depending on which set
    the corresponding image belongs to."""
    for k, v in split_dict.items():
        for _img_name in v:
            annotations.loc[annotations[index_column_name] == _img_name, 'set'] = k
    return annotations


def create_yolo_annotation_line(category_id_no: int, bbox: List[float]) -> str:
    """
    Takes a cateogry id and yolo-formatted bbox coordinates and returns a string to be used in the annotation file."""
    logging.debug(f"Cat: {category_id_no}, bbox: {bbox}")
    category_id = str(category_id_no)
    _bbox_annotation = category_id
    for boxval in bbox:
        _bbox_annotation = ' '.join([_bbox_annotation, str(boxval)])
    return _bbox_annotation


def create_yolo_file(fpath_dst, yolo_lines: list = None) -> None:
    if yolo_lines is None:
        yolo_lines = []
    with open(fpath_dst, "w") as f:
        f.writelines(yolo_lines)


def cvt_labelme_to_yolo_annotation(fpath_labelme_json, materials_dict=None):
    """
    Converts a labelme .json to a yolo .txt annotation in the same folder. Assumes the corresponding image is also in
    that folder.
    :param fpath_labelme_json:
    :param materials_dict:
    :return:
    """
    root_dir, fname = os.path.split(fpath_labelme_json)
    basename, _ = os.path.splitext(fname)

    if materials_dict is None:
        materials: list = ds_annotations.get_materials_from_labelme_jsons(root_dir)
        materials_dict = ds_annotations.create_materials_dict(materials)
    materials_dict_flipped = invert_dictionary(materials_dict)

    labelme_annotation = load_json(fpath_labelme_json)
    fpath_img = os.path.join(root_dir, labelme_annotation["imagePath"])

    yolo_lines = []
    for annotation in labelme_annotation["shapes"]:
        img_height, img_width, channels = cv2.imread(fpath_img).shape
        material_id: int = materials_dict_flipped[annotation["label"]]
        bbox = annotation["points"]
        bbox = bbox_conversions.fix_labelme_point_order(bbox)
        yolo_bbox: List[float] = bbox_conversions.labelme_to_yolo(bbox, img_width, img_height)

        if not bbox_conversions.yolo_bbox_is_within_bounds(yolo_bbox):
            print(f"Invalid yolo bbox: {yolo_bbox} file {fpath_labelme_json}")

        yolo_bbox: List[str] = [str(n) for n in yolo_bbox]
        line = f"{material_id} {' '.join(yolo_bbox)}\n"
        yolo_lines.append(line)

    fpath_yolo_annotation = f"{root_dir}/{basename}.txt"
    create_yolo_file(fpath_yolo_annotation, yolo_lines)


# def create_yolo_annotations(fdir_labelme, save_materials_dict=False) -> dict:
#     """
#     Very slow for some reason.
#     Non-recursive!\n
#     Creates yolo-styled annotation files in the folder where the image and json files from labelme are located.
#
#     :param fdir_labelme: path to the directory that contains image and json files.
#     :return: materials dict
#     """
#     materials: list = ds_annotations.get_materials_from_labelme_jsons(fdir_labelme, recursive=False)
#     materials_dict = ds_annotations.create_materials_dict(materials)
#     print('Creating yolo annotation files...')
#     pairs = get_img_and_json_file_pairs(fdir_labelme)
#     for i, (fpath_img, fpath_json) in enumerate(pairs):
#         if fpath_json is not None:
#             cvt_labelme_to_yolo_annotation(fpath_json, materials_dict)
#         else:
#             fpath_yolo_annotation = f"{fpath_img.rsplit('.')[0]}.txt"
#             create_yolo_file(fpath_yolo_annotation)
#
#         if i % 100 == 0:
#             print(f"Processed {i + 1} out of {len(pairs)}.")
#
#     if save_materials_dict:
#         dst_mats_dict = os.path.join(fdir_labelme, "materials.json")
#         with open(dst_mats_dict, "w") as f:
#             f.write(json.dumps(materials_dict, indent=2))
#
#     return materials_dict


def create_yolo_annotations(fdir_labelme, save_materials_dict):
    """
    Non-recursive!\n
    Creates yolo-styled annotation files in the folder where the image and json files from labelme are located.

    :param fdir_labelme: path to the directory that contains image and json files.
    :param fpath_dst_mats_dict: target path for materials dict json file.
    :return: df, mats_dict.
    """
    materials = ds_annotations.get_materials_from_labelme_jsons(fdir_labelme, recursive=False)
    materials_dict = ds_annotations.create_materials_dict(materials)

    print('Starting dataframe...')
    img_list = list_image_names(fdir_labelme)
    json_list = list_json_names(fdir_labelme)
    df_joined = join_json_and_img_lists(img_list, json_list)
    df_joined = add_img_dims(df_joined, fdir_labelme)
    logging.debug(f"Joined df columns: {df_joined.columns}")

    df_joined.to_csv("/home/findux/Desktop/df.csv")

    print('Creating annotation files...')
    all_annotations = []
    for i, line in df_joined.iterrows():
        annotation_file_path = os.path.join(fdir_labelme, line['id_name'] + '.txt')
        img_annotations = []
        if not pd.isna(line['json_name']):
            json_path = os.path.join(fdir_labelme, line['json_name'])
            json_file = load_json(json_path)
            for bbox in json_file['shapes']:
                points = bbox['points']
                labelme_bbox = bbox_conversions.fix_labelme_point_order(points)
                material = bbox['label']
                # Find the index corresponding to the material
                material_i = list(materials_dict.keys())[list(materials_dict.values()).index(material)]
                try:
                    yolo_bbox = bbox_conversions.labelme_to_yolo(labelme_bbox, line['img_width'], line['img_height'])
                except BoxFormatError:
                    print(f"json: {json_path}")
                    sys.exit(1)
                annotation_line = create_yolo_annotation_line(material_i, yolo_bbox)
                img_annotations.append(annotation_line + '\n')
        with open(annotation_file_path, 'w') as f:
            f.writelines(img_annotations)
        all_annotations.append(img_annotations)
    logging.info(all_annotations)
    df_joined['annotations'] = all_annotations

    if save_materials_dict:
        dst_mats_dict = os.path.join(fdir_labelme, "materials.json")
        with open(dst_mats_dict, "w") as f:
            f.write(json.dumps(materials_dict, indent=2))

    # df_joined.to_csv("/home/findux/Desktop/df_joined.csv")
    print("Done.")
    return df_joined, materials_dict



def create_yolo_directories(target_directory: str, exist_ok=False) -> dict:
    """
    Creates the target directory, with subfolders according to yolo requirements. Also creates a "..._testing" folder in
    the parent directory.
    :param target_directory: str
    :return: dictionary with target directory paths
    """
    path_img_train = os.path.join(target_directory, 'images/train')
    path_img_val = os.path.join(target_directory, 'images/valid')
    path_img_test = os.path.join(target_directory, 'images/test')

    path_labels_train = os.path.join(target_directory, 'labels/train')
    path_labels_val = os.path.join(target_directory, 'labels/valid')
    path_labels_test = os.path.join(target_directory, 'labels/test')
    try:
        os.makedirs(target_directory, exist_ok=exist_ok)
        os.makedirs(path_img_train, exist_ok=exist_ok)
        os.makedirs(path_img_val, exist_ok=exist_ok)
        os.makedirs(path_img_test, exist_ok=exist_ok)
        os.makedirs(path_labels_train, exist_ok=exist_ok)
        os.makedirs(path_labels_val, exist_ok=exist_ok)
        os.makedirs(path_labels_test, exist_ok=exist_ok)
        print('Created directories.')
    except FileExistsError:
        raise FileExistsError('One or more target directories already exist.')
    else:
        directories = {'images': {'train': path_img_train, 'val': path_img_val, 'test': path_img_test},
                       'labels': {'train': path_labels_train, 'val': path_labels_val, 'test': path_labels_test}}
        return directories


def create_yolo_dataset(fdir_src: str, fdir_dst: str = None,
                        instance_column_name: str = 'file_name', train_val_test: Tuple = (0.6, 0.2, 0.2),
                        materials_dict = None, exist_ok=False, seed: int = 42) -> None:
    """
    Creates a yolo dataset from the img and yolo annotation files in a folder.
    :param fdir_src:
    :param fdir_dst:
    :param instance_column_name:
    :param train_val_test:
    :param seed:
    :return:
    """

    # ToDo: maybe skip the entire dataframe, just work with tuples that contain the corresponding img/txt paths.
    # ToDo: Also: just check that each image has a (and just one) corresponding text file. We don't care if there are
    #       leftover txt files. Maybe raise a warning if you encounter some, but don't stop.

    if fdir_dst is None:
        fdir_dst = f"{fdir_src.rstrip('/')}_yolo"
    if materials_dict is None:
        materials = ds_annotations.get_materials_from_labelme_jsons(fdir_src)
        materials_dict = ds_annotations.create_materials_dict(materials)

    # ToDo: use either the dataframe or the folder. think about this
    #       the df needs a path column for both the images and the files. Or one general path that stops before the extension?

    # Check if files have corresponding equivalents:
    if ds_annotations.all_imgs_have_yolo_annotation(fdir_src):
        print("All imgs have a corresponding txt file.")
    else:
        print("Not all images have a corresponding text file. (Re-)creating txt files from jsons...")
        create_yolo_annotations(fdir_src, save_materials_dict=False)

    files_dataframe = create_files_dataframe(fdir_src)
    # Find individual file names
    instances = list(files_dataframe[instance_column_name])
    # Create training, validation and test sets
    sets = ds_split.split_instance_list_to_train_val_test(instances, prop_train_val_test=train_val_test, seed=seed)
    # Merge this info into the df
    files_dataframe = add_set_column(files_dataframe, sets)
    # Create target dirs
    target_dirs = create_yolo_directories(target_directory=fdir_dst, exist_ok=exist_ok)
    # Copy files
    copy_yolo_files(files_dataframe, target_dirs)
    # Create dataset.yaml
    print(f"Creating dataset.yaml ...")
    yolo_tools.create_yolo_ds_yaml(fdir_dst, materials_dict=materials_dict)
    print(f"Saving materials in materials_dict.json ...")
    ds_annotations.save_materials_dict(materials_dict, fdir_dst)

    print(f'Yolo dataset creation complete: {fdir_dst}')


def create_yolo_ds_from_labelme_dir(labelme_root, target_dir, train_val_test=(0.7, 0.2, 0.1), exist_ok=False, seed=42):
    materials_dict = create_yolo_annotations(labelme_root, )
    create_yolo_dataset(fdir_src=labelme_root, fdir_dst=target_dir, train_val_test=train_val_test,
                        materials_dict=materials_dict, exist_ok=exist_ok, seed=seed)


def join_json_and_img_lists(img_list: List[str], json_list: List[str]) -> pd.DataFrame:
    """
    Joins a img and json list into a data frame with indexes.
    :param img_list:
    :param json_list:
    :return:
    """
    file_id = [os.path.splitext(fname)[0] for fname in img_list]
    # Make sure there are no duplicates (e.g. if the same image exists in two formats):
    assert len(file_id) == len(set(file_id))
    img_df = pd.DataFrame({'id_name': file_id, 'img_name': img_list}).set_index('id_name')
    json_ids = [os.path.splitext(jname)[0] for jname in json_list]
    json_df = pd.DataFrame({'id_name': json_ids, 'json_name': json_list}).set_index('id_name')
    joined_df = img_df.join(json_df, on='id_name', how='left')
    joined_df = joined_df.reset_index()
    return joined_df


def load_json(json_fpath: str) -> dict:
    """Returns json data as a dict."""
    with open(json_fpath, 'r') as f:
        data = json.load(f)
    logging.info(f'Loaded json object (type): {type(data)}')
    return data


def list_image_names(img_dir: str) -> List[str]:
    """Non-recursive!\n
    Returns a (sorted) list of filenames of images in a folder that can be opened by PIL.Image.open(). Note that
    they might be of various filetypes. Ignores files that can not be opened by PIL.Image.open()."""
    _files = sorted(os.listdir(img_dir))
    images = []
    for _fname_img in _files:
        try:
            _ = Image.open(os.path.join(img_dir, _fname_img))
        # Skip files that are not readable as img, and directories.
        except (UnidentifiedImageError, IsADirectoryError):
            logging.debug(f'{_fname_img} is not a readable image.')
        else:
            images.append(_fname_img)
    return images


def copy_imgs_w_json(fdir_src, fdir_dst):
    """
    Copies image and json files, but only those for which there IS a corresponding json file (i.e. empty images are not
    copied)
    :param fdir_src:
    :param fdir_dst:
    :return:
    """
    if not os.path.isdir(fdir_dst):
        os.makedirs(fdir_dst)

    file_pairs = get_img_and_json_file_pairs(fdir_src)
    for (src_img, src_json) in file_pairs:
        logging.info(f"JSON_SOURCE: {src_json}")
        logging.info(f"IMG_SOURCE: {src_img}")
        for src in (src_img, src_json):
            logging.info(f"SOURCE: {src}")
            dst = os.path.join(fdir_dst, os.path.split(src)[-1])
            logging.info(f"DESTIN: {dst}")
            shutil.copyfile(src, dst)
    print("Done")


def list_json_names(fdir: str) -> List[str]:
    """Non-recursive!\n
    Returns an ordered list of all the json filenames in fdir."""
    json_fnames = [file for file in sorted(os.listdir(fdir)) if file.endswith('.json')]
    assert len(json_fnames) == len(set(json_fnames))  # Make sure fnames are unique.
    return json_fnames


def copy_yolo_files(files_df: pd.DataFrame, target_dirs: dict):
    """
    Copies images and yolo annotation files according to a dictionary that contains target directories (for train, val
    and test), and an annotations_df dataframe that has info on which image belongs to which set.
    """
    files_df_reduced = files_df.drop_duplicates(subset='file_name')
    assert len(files_df_reduced['file_name']) ==\
           len(set(files_df['file_name'])) ==\
           len(set(files_df_reduced['file_name']))

    print("Copying images and annotation files...")
    for i, line in files_df.iterrows():
        _current_set = line['set']
        _img_fname = line['img_name']
        _img_source_path = line['img_fpath']
        _annotation_fname = line['annotation_name']
        _annotation_source_path = line['annotation_fpath']

        # Copy img
        _img_target_path = os.path.join(target_dirs['images'][_current_set], _img_fname)
        shutil.copyfile(_img_source_path, _img_target_path)
        # Copy annotation file
        _annot_target_path = os.path.join(target_dirs['labels'][_current_set], _annotation_fname)
        shutil.copyfile(_annotation_source_path, _annot_target_path)

    logging.info(f'Copied {i + 1} images.')
    print('Done copying.')


def create_files_dataframe(fpath: str) -> pd.DataFrame:
    """
    :param fpath:
    :return:
    """
    # Instead of the following, perhaps use a set of allowed image extensions?
    # img_files = [file for file in sorted(os.listdir(fpath)) if is_valid_img(os.path.join(fpath, file))]
    img_files = [file for file in sorted(os.listdir(fpath)) if file.lower().endswith(YOLO_IMG_FORMATS)]
    annotation_files = [file for file in sorted(os.listdir(fpath)) if file.lower().endswith('.txt')]
    # Verify same names:
    img_names_only = [fname.rsplit('.')[0] for fname in img_files]
    annotation_names_only = [fname.rsplit('.')[0] for fname in annotation_files]
    assert len(img_files) == len(annotation_files)
    assert len(img_names_only) == len(annotation_names_only)
    assert img_names_only == annotation_names_only
    file_dataframe = pd.DataFrame({'file_name': img_names_only,
                                   'img_name': img_files,
                                   'img_fpath': [os.path.join(fpath, imgfile) for imgfile in img_files],
                                   'annotation_name': annotation_files,
                                   'annotation_fpath': [os.path.join(fpath, annotfile) for annotfile in annotation_files]})
    return file_dataframe


def extract_paths_to_yolo_ds_files(fpath_yolo_ds) -> Dict[str, Dict[str, list]]:
    """
    Returns a dictionary of the file paths to the different yolo dataset folders.
    :param fpath_yolo_ds:
    :return:
    """
    train_img_dir = os.path.join(fpath_yolo_ds, "images/train")
    val_img_dir = os.path.join(fpath_yolo_ds, "images/valid")
    test_img_dir = os.path.join(fpath_yolo_ds, "images/test")

    train_labs_dir = os.path.join(fpath_yolo_ds, "labels/train")
    val_labs_dir = os.path.join(fpath_yolo_ds, "labels/valid")
    test_labs_dir = os.path.join(fpath_yolo_ds, "labels/test")

    logging.info(train_img_dir)
    logging.info(test_img_dir)
    logging.info(val_img_dir)
    logging.info(train_labs_dir)
    logging.info(test_labs_dir)
    logging.info(val_labs_dir)

    train_imgs = [os.path.join(train_img_dir, file) for file in os.listdir(train_img_dir)]
    val_imgs = [os.path.join(val_img_dir, file) for file in os.listdir(val_img_dir)]
    test_imgs = [os.path.join(test_img_dir, file) for file in os.listdir(test_img_dir)]

    train_labs = [os.path.join(train_labs_dir, file) for file in os.listdir(train_labs_dir)]
    val_labs = [os.path.join(val_labs_dir, file) for file in os.listdir(val_labs_dir)]
    test_labs = [os.path.join(test_labs_dir, file) for file in os.listdir(test_labs_dir)]

    return {"images": {"train": train_imgs,
                       "valid": val_imgs,
                       "test": test_imgs},
            "labels": {"train": train_labs,
                       "valid": val_labs,
                       "test": test_labs}}


def initiate_coco_dict(ds_name_or_description: str, materials_dict: dict, **kwargs):
    """
    :param ds_name_or_description:
    :param materials_dict:
    :param kwargs: year: int, version: str, contributor: str, date_created: str
    :return:
    """
    # ToDo: Maybe turn this into a class that is easily appendable. Provide a function that reads everything from a coco
    #       or yolo ds and updates the class.
    materials_dict_list = ds_annotations.create_coco_materials_dicts(materials_dict)
    coco_dict = {"info": {"year": int(datetime.date.today().year),
                          "version": kwargs.get("version", None),
                          "description": ds_name_or_description,
                          "contributor": kwargs.get("contributor", "BIOBLU project, University of Malta"),
                          "date_created": kwargs.get("date_created", str(datetime.date.today())),
                          },
                 "images": [],
                 "annotations": [],
                 "categories": materials_dict_list,
                 "licences": [],
                 }
    return coco_dict


def create_coco_json_from_copied_yolo_set(yolo_root_dir: str, coco_root_dir: str, ds_source_set: str,
                                          target_save_file: str,
                                          materials_dict: dict = None) -> None:
    """
    Creates json files for a coco-styled dataset that has been copied. Does not use the old image locations, but their
    new location in a coco-styled directory tree.
    Creates a json file from a yolo dataset. Using ds_set, either train, valid or test set can be specified.
    :param yolo_root_dir: Yolo root directory. Needs to have subfolders "images" and "labels", each wih subfolders "train", "test" and "valid"
    :param coco_root_dir: COCO root directory.
    :param ds_source_set: Can be either "train", "test", "valid"
    :param target_save_file: json output file path
    :param materials_dict: material dict , e.g. {0: 'plastic'}
    :return: None. Creates a json file.
    ToDo: Perhaps add **kwargs for licenses and capture dates
    ToDo: Define functions for initiating and updating coco jsons, so that the loops do not show up in two different places
    """
    set_names = {"val": "val",
                 "valid": "val",
                 "train": "train",
                 "test": "test"}
    assert ds_source_set.lower() in set_names.keys()

    if not os.path.isdir(coco_root_dir):
        logging.info(f"Coco-style root ds does not exist. Creating {coco_root_dir}")
        os.makedirs(coco_root_dir)

    if materials_dict is None:
        materials_dict = bioblu.ds_manage.file_ops.load_json(os.path.join(yolo_root_dir, "materials_dict.json"))

    materials_dict_list = ds_annotations.create_coco_materials_dicts(materials_dict)
    inverted_mats_dict = {v: k for k, v in materials_dict.items()}

    logging.info(f"Mats dict list: {materials_dict_list}")
    logging.info(f"Mats dict: {materials_dict}")
    logging.info(f"Inv. mats dict: {inverted_mats_dict}")

    img_source_dir = os.path.join(yolo_root_dir, "images", ds_source_set.lower())
    logging.info(f"Img dir: {img_source_dir}")
    labels_source_dir = os.path.join(yolo_root_dir, "labels", ds_source_set.lower())
    logging.info(f"Labels dir: {labels_source_dir}")

    # ToDo: Instead of re-creating the paths where the images SHOULD be, recursively list the contents.
    #       That would probably also be less error prone, as long as theres an name-mismatch error catch.
    # img_src_paths = [os.path.join(img_source_dir, fname) for fname in sorted(os.listdir(img_source_dir))]
    # img_target_paths = [os.path.join(coco_root_dir, set_names[ds_source_set], fname) for fname in sorted(os.listdir(img_source_dir))]
    img_src_paths = bioblu.ds_manage.file_ops.get_all_fpaths_by_extension(img_source_dir, YOLO_IMG_FORMATS)

    img_target_paths = [os.path.join(coco_root_dir, set_names[ds_source_set], fname) for fname in sorted(os.listdir(img_source_dir))]
    # labels_src_paths = [os.path.join(labels_source_dir, labfname) for labfname in sorted(os.listdir(labels_source_dir))]
    labels_src_paths = bioblu.ds_manage.file_ops.get_all_fpaths_by_extension(labels_source_dir, (".txt",))
    logging.debug(f"Img. src path count: {len(img_src_paths)}")
    logging.debug(f"Img. dst path count: {len(img_target_paths)}")
    logging.debug(f"Lab. src path count: {len(labels_src_paths)}")
    assert len(img_src_paths) == len(labels_src_paths)


    logging.info("Creating coco-style dict...")
    coco_dict = initiate_coco_dict(f"dataset created from yolo {yolo_root_dir}", materials_dict)

    box_id_counter = 0
    for i, (img_src_path, label_path, img_target_path) in enumerate(zip(img_src_paths, labels_src_paths, img_target_paths)):
        basename_img = os.path.split(img_src_path)[-1].split(".")[0]
        basename_annotations = os.path.split(label_path)[-1].split(".")[0]
        if basename_img != basename_annotations:
            raise AssertionError(f"[ WARNING ] Names of Annotation and image file do not match: img: {basename_img}, annots: {basename_annotations}")
        coco_dict["images"].append({"id": i,
                                    "width": Image.open(img_src_path).size[0],
                                    "height": Image.open(img_src_path).size[1],
                                    "file_name": img_target_path,  # "file_name": os.path.split(img_path)[-1],
                                    "license": None,
                                    "flickr_url": None,
                                    "coco_url": None,
                                    "date_captured": None,
                                    })
        yolo_boxes = ds_annotations.load_yolo_annotations_as_BBoxes(label_path, img_src_path, materials_dict)
        for box in yolo_boxes:
            old_box = box.bbox
            box.to_coco()
            new_box = box.bbox
            logging.debug(f"Old v. new bbox: {old_box} -> {new_box}")
            coco_dict["annotations"].append({"id": box_id_counter,
                                             "image_id": i,
                                             "category_id": inverted_mats_dict[box.material],
                                             "segmentation": [],
                                             "area": None,
                                             "iscrowd": 0,
                                             "bbox": box.bbox,
                                             "bbox_mode": BoxMode.XYWH_ABS,
                                             })
            assert len(coco_dict["annotations"][-1]["bbox"]) == 4
            box_id_counter += 1

    with open(target_save_file, "w") as f:
        json.dump(coco_dict, f, indent=4)
    logging.info(f"Coco-styled json saved to {target_save_file}")


def create_one_coco_json_only_from_yolo_set(yolo_root_dir: str, ds_source_set: str,
                                            target_save_file: str, materials_dict: dict = None) -> None:
    """
    Creates a single json file from a yolo dataset. Using ds_set, either train, valid or test set can be specified.
    Does not move or copy images from the yolo ds.
    :param yolo_root_dir: Yolo root directory. Needs to have subfolders "images" and "labels", each wih subfolders "train", "test" and "valid"
    :param ds_source_set: Can be either "train", "test", "valid"
    :param target_save_file: json output file path
    :param materials_dict: material dict , e.g. {0: 'plastic'}
    :return: None. Creates a json file.
    ToDo: Perhaps add **kwargs for licenses and capture dates
    """
    set_names = {"val": "val",
                 "valid": "val",
                 "train": "train",
                 "test": "test"}
    assert ds_source_set.lower() in set_names.keys()

    if materials_dict is None:
        materials_dict = ds_annotations.create_fallback_yolo_materials_dict(yolo_root_dir)
        logging.info(f"No materials dict provided. Created fallback dict: {materials_dict}")
    materials_dict_list = ds_annotations.create_coco_materials_dicts(materials_dict)
    inverted_mats_dict = {v: k for k, v in materials_dict.items()}
    logging.info(f"Mats dict list: {materials_dict_list}")
    logging.info(f"Mats dict: {materials_dict}")
    logging.info(f"Inv. mats dict: {inverted_mats_dict}")

    img_source_dir = os.path.join(yolo_root_dir, "images", ds_source_set.lower())
    logging.info(f"Img dir: {img_source_dir}")
    labels_source_dir = os.path.join(yolo_root_dir, "labels", ds_source_set.lower())
    logging.info(f"Labels dir: {labels_source_dir}")

    img_src_paths = [os.path.join(img_source_dir, fname) for fname in sorted(os.listdir(img_source_dir))]
    labels_src_paths = [os.path.join(labels_source_dir, labfname) for labfname in sorted(os.listdir(labels_source_dir))]
    assert len(img_src_paths) == len(labels_src_paths)

    logging.info("Creating coco-style dict...")
    coco_dict = initiate_coco_dict(f"dataset created from yolo {yolo_root_dir}", materials_dict)

    box_id_counter = 0
    for i, (img_src_path, label_path) in enumerate(zip(img_src_paths, labels_src_paths)):
        basename_img = os.path.split(img_src_path)[-1].split(".")[0]
        basename_annotations = os.path.split(label_path)[-1].split(".")[0]
        if basename_img != basename_annotations:
            raise AssertionError(f"[ WARNING ] Names of Annotation and image file do not match: img: {basename_img}, annots: {basename_annotations}")
        coco_dict["images"].append({"id": i,
                                    "width": Image.open(img_src_path).size[0],
                                    "height": Image.open(img_src_path).size[1],
                                    "file_name": img_src_path,  # "file_name": os.path.split(img_path)[-1],
                                    "license": None,
                                    "flickr_url": None,
                                    "coco_url": None,
                                    "date_captured": None,
                                    })
        yolo_boxes = ds_annotations.load_yolo_annotations_as_BBoxes(label_path, img_src_path, materials_dict)
        for box in yolo_boxes:
            old_box = box.bbox
            box.to_coco()
            new_box = box.bbox
            logging.debug(f"Old v. new bbox: {old_box} -> {new_box}")
            coco_dict["annotations"].append({"id": box_id_counter,
                                             "image_id": i,
                                             "category_id": inverted_mats_dict[box.material],
                                             "segmentation": [],
                                             "area": None,
                                             "iscrowd": 0,
                                             "bbox": box.bbox,
                                             "bbox_mode": BoxMode.XYWH_ABS,
                                             })
            assert len(coco_dict["annotations"][-1]["bbox"]) == 4
            box_id_counter += 1

    with open(target_save_file, "w") as f:
        json.dump(coco_dict, f, indent=4)
    logging.info(f"Coco-styled json saved to {target_save_file}")


def create_coco_jsons_only_from_yolo(yolo_root_dir: str, json_target_dir: str = None, dataset_name: str = None,
                                materials_dict=None) -> None:
    """
    Creates only the coco-styled jsons for a yolo dataset, pointing to the images in the yolo ds,
    but does not copy or move the images inside the yolo ds.
    :param yolo_root_dir:
    :param json_target_dir:
    :param dataset_name:
    :param materials_dict:
    :return:
    """
    if json_target_dir is None:
        _split_path = [e for e in yolo_root_dir.split('/') if e][:-1]  # rm empty elements
        json_target_dir = os.path.join('/', *_split_path)
    if dataset_name is None:
        _split_path = [e for e in yolo_root_dir.split('/') if e]  # rm empty elements
        dataset_name = _split_path[-1] + "_detectron"
    if materials_dict is None:
        materials_dict = ds_annotations.create_fallback_yolo_materials_dict(yolo_root_dir)
    print(f"Dataset name: {dataset_name}")
    print(f"Saving jsons in location: {json_target_dir}")
    print(f"Materials: {materials_dict}")

    fpath_json_train = os.path.join(json_target_dir, "instances_" + dataset_name + "_train.json")
    fpath_json_val = os.path.join(json_target_dir, "instances_" + dataset_name + "_val.json")
    fpath_json_test = os.path.join(json_target_dir, "instances_" + dataset_name + "_test.json")

    # Create json files:
    create_one_coco_json_only_from_yolo_set(yolo_root_dir=yolo_root_dir, ds_source_set="train",
                                            target_save_file=fpath_json_train, materials_dict=materials_dict)
    create_one_coco_json_only_from_yolo_set(yolo_root_dir=yolo_root_dir, ds_source_set="valid",
                                            target_save_file=fpath_json_val, materials_dict=materials_dict)
    create_one_coco_json_only_from_yolo_set(yolo_root_dir=yolo_root_dir, ds_source_set="test",
                                            target_save_file=fpath_json_test, materials_dict=materials_dict)
    print("Done creating jsons.")


def cvt_yolo_to_detectron(yolo_root_dir: str, fdir_dst: str = None, dataset_name: str = "detectron",
                          materials_dict: dict = None, exist_ok = False) -> None:
    """
    Converts a yolo dataset to a coco-styled dataset (but does not pretend it is a genuine COCO dataset such as e.g.
    coco2017).
    Yolo bboxes are (xc, yc, w, h) (relative to img dims), detectron bboxes have COCO format: (x0, y0, w, h) (px).

    :param yolo_root_dir: yolo root ds dir
    :param fdir_dst: optional. target root location of coco target dir.
    :param materials_dict: e.g. {0: "trash"}
    :return:
    """

    # ToDo: As yolo creation now also includes automated dataset.yaml creation, maybe read the materials from there?
    print(f"Converting {yolo_root_dir.split('/')[-1]} to detectron format.")
    print(termcolor.colored("[ WARNING ]", color="red") + f" The detectron dataset being created now cannot be moved"
                                                          f" because file paths in jsons would not match afterwards.")
    if fdir_dst is None:
        fdir_dst = yolo_root_dir.rstrip("/") + "_detectron"
    print(f"Saving converted detectron2 dataset in: {os.path.abspath(fdir_dst)}")

    print("Creating coco directories and paths...")
    target_annotations_dir = os.path.join(fdir_dst, "annotations")
    imgs_train_target_dir = os.path.join(fdir_dst, "train")
    imgs_valid_target_dir = os.path.join(fdir_dst, "val")
    imgs_test_target_dir = os.path.join(fdir_dst, "test")

    if os.path.isdir(fdir_dst) and not exist_ok:
        print(termcolor.colored("[ WARNING ]", "red", attrs=['blink']) + f" Dataset conversion skipped. Target dir already exists: {fdir_dst}")
        return None
    else:
        if os.path.isdir(fdir_dst):
            print(termcolor.colored("[ WARNING ]", color="red") + " Overwriting existing dataset.")
        os.makedirs(target_annotations_dir, exist_ok=exist_ok)
        os.makedirs(imgs_train_target_dir, exist_ok=exist_ok)
        os.makedirs(imgs_valid_target_dir, exist_ok=exist_ok)
        os.makedirs(imgs_test_target_dir, exist_ok=exist_ok)
    print("Creating coco jsons...")

    if materials_dict is None:
        fpath_mats_dict = os.path.join(yolo_root_dir, "materials_dict.json")
        try:
            materials_dict = bioblu.ds_manage.file_ops.load_json(fpath_mats_dict)
            shutil.copyfile(fpath_mats_dict, os.path.join(fdir_dst, os.path.split(fpath_mats_dict)[-1]))
        except FileNotFoundError:
            print(f"Did not find materials_dict.json")
            ds_annotations.create_fallback_yolo_materials_dict(yolo_root_dir)
        else:
            materials_dict = {int(k): v for k, v in materials_dict.items()}
            print(f"Loaded materials dict from {materials_dict}")

    # Create json target paths
    train_json_name = os.path.join(target_annotations_dir, "instances_" + dataset_name + "_train.json")
    val_json_name = os.path.join(target_annotations_dir, "instances_" + dataset_name + "_val.json")
    test_json_name = os.path.join(target_annotations_dir, "instances_" + dataset_name + "_test.json")

    # Create json files:
    create_coco_json_from_copied_yolo_set(yolo_root_dir=yolo_root_dir, coco_root_dir=fdir_dst, ds_source_set="train",
                                          target_save_file=train_json_name, materials_dict=materials_dict)
    create_coco_json_from_copied_yolo_set(yolo_root_dir=yolo_root_dir, coco_root_dir=fdir_dst, ds_source_set="valid",
                                          target_save_file=val_json_name, materials_dict=materials_dict)
    create_coco_json_from_copied_yolo_set(yolo_root_dir=yolo_root_dir, coco_root_dir=fdir_dst, ds_source_set="test",
                                          target_save_file=test_json_name, materials_dict=materials_dict)
    print("Getting yolo file paths...")

    # Yolo img source dirs
    yolo_train_img_source_dir = os.path.join(yolo_root_dir, "images/train")
    yolo_valid_img_source_dir = os.path.join(yolo_root_dir, "images/valid")
    yolo_test_img_source_dir = os.path.join(yolo_root_dir, "images/test")

    # Yolo img sources (indiv. paths)
    train_img_sources = [os.path.join(yolo_train_img_source_dir, fname) for fname in os.listdir(yolo_train_img_source_dir)]
    valid_img_sources = [os.path.join(yolo_valid_img_source_dir, fname) for fname in os.listdir(yolo_valid_img_source_dir)]
    test_img_sources = [os.path.join(yolo_test_img_source_dir, fname) for fname in os.listdir(yolo_test_img_source_dir)]

    # Image target paths in coco ds
    train_img_targets = [os.path.join(imgs_train_target_dir, os.path.split(fpath)[-1]) for fpath in train_img_sources]
    valid_img_targets = [os.path.join(imgs_valid_target_dir, os.path.split(fpath)[-1]) for fpath in valid_img_sources]
    test_img_targets = [os.path.join(imgs_test_target_dir, os.path.split(fpath)[-1]) for fpath in test_img_sources]

    logging.debug(f"Training img. targets: {train_img_targets}")
    logging.debug(f"Validation img. targets: {valid_img_targets}")

    logging.info(f" Len train src/trg: {len(train_img_sources)}/{len(train_img_targets)}")
    logging.info(f" Len valid src/trg: {len(valid_img_sources)}/{len(valid_img_targets)}")
    logging.info(f" Len test src/trg: {len(test_img_sources)}/{len(test_img_targets)}")

    assert len(train_img_sources) == len(train_img_targets)
    assert len(valid_img_sources) == len(valid_img_targets)
    assert len(test_img_sources) == len(test_img_targets)

    print("Copying images from yolo to detectron ds...")

    # Create one long sources list
    sources = train_img_sources
    sources.extend(valid_img_sources)
    sources.extend(test_img_sources)

    # Create one long target list
    targets = train_img_targets
    targets.extend(valid_img_targets)
    targets.extend(test_img_targets)
    assert len(sources) == len(targets)

    # Copy files
    file_count = len(sources)
    for i, (src, trg) in enumerate(zip(sources, targets)):
        # Make sure it's the same file name.
        src_name = os.path.split(src)[-1]
        trg_name = os.path.split(trg)[-1]
        assert src_name == trg_name
        # Actually copy file
        shutil.copyfile(src, trg)
        if i % 25 == 0 and i > 0:
            print(f"Copied {i:03d}/{file_count} files.")  # 03d specifies 3 digit zero padding
    print("Yolo to detectron conversion finished.")


def get_img_and_json_file_pairs(fdir):
    """
    Returns tuples with the corresponding img and json file.
    :param fdir:
    :return: List of tuples [(fpath_img, fpath_json), ...]
    """
    fpaths_imgs = bioblu.ds_manage.file_ops.get_all_fpaths_by_extension(fdir, YOLO_IMG_FORMATS)
    pairs = []
    imgs_without_json = []
    for fpath_img in fpaths_imgs:
        corresponding_json = bioblu.ds_manage.file_ops.get_corresponding_file(fpath_img, fdir, ("json",))
        if corresponding_json:
            pairs.append((fpath_img, corresponding_json))
        else:
            imgs_without_json.append(os.path.split(fpath_img)[-1])
    if imgs_without_json:
        print(f"Images w/o json: {imgs_without_json}")
    return pairs


def get_yolo_img_annotation_pairs(yolo_root_dir: str) -> List[Tuple[str, str]]:
    """
    Returns a list of tuples with the (img_path, txt_path) for a yolo dataset. Works recursively and iterates through all
    subfolders.

    :param yolo_base_dir:
    :return: List of tuptes: [(fpath_img, fpath_txt), ...]
    """

    # ToDo: speed this up by following the fixed file structure

    fpaths_imgs = bioblu.ds_manage.file_ops.get_all_fpaths_by_extension(yolo_root_dir, YOLO_IMG_FORMATS)
    fpaths_txts = bioblu.ds_manage.file_ops.get_all_fpaths_by_extension(yolo_root_dir, (".txt",))

    pairs = []
    for fpath_img in fpaths_imgs:
        basename_img = bioblu.ds_manage.file_ops.get_basename_only(fpath_img)
        corresponding_txt_files = []
        for fpath_txt in fpaths_txts:
            basename_txt = bioblu.ds_manage.file_ops.get_basename_only(fpath_txt)
            if basename_img == basename_txt:
                logging.debug(f"{basename_txt} == {basename_img}")
                corresponding_txt_files.append(fpath_txt)

        if not corresponding_txt_files:
            print(f"Base {fpath_img} does not have a corresponding txt file.")
        elif len(corresponding_txt_files) > 1:
            print(f"Base {basename_img} has multiple correspondances: {corresponding_txt_files}")
        elif len(corresponding_txt_files) == 1:
            current_pair = (fpath_img, corresponding_txt_files[0])
            logging.info(f"Basename img: {basename_img}, current pair: {current_pair}")
            assert bioblu.ds_manage.file_ops.get_basename_only(current_pair[0]) == bioblu.ds_manage.file_ops.get_basename_only(current_pair[1])
            pairs.append(current_pair)

    for img, txt in pairs:
        base_img = bioblu.ds_manage.file_ops.get_basename_only(img)
        base_txt = bioblu.ds_manage.file_ops.get_basename_only(txt)
        assert base_img == base_txt

    return pairs


def cvt_taco_to_yolo(taco_root: str, fdir_dst):
    if not os.path.isdir(fdir_dst):
        os.makedirs(fdir_dst)

    annotations_json: str = taco_root + "/data/annotations.json"

    imgs: pd.DataFrame
    labels: pd.DataFrame
    imgs, labels = ds_annotations.load_coco_ds(annotations_json)
    imgs["file_name"] = taco_root + "/data/" + imgs["file_name"]  # Use absolute path

    # Merge
    annotations_table: pd.DataFrame = ds_annotations.merge_img_info_into_labels(imgs, labels)
    # Add yolo-style labels
    yolo_annotations: pd.DataFrame = ds_annotations.cvt_df_coco_bbox_annotations_to_yolo(annotations_table)
    # Unique images
    img_paths: np.ndarray = yolo_annotations["file_name"].unique()
    print(f"{img_paths.shape[0]} images found.")


    for i, img_fpath in enumerate(img_paths):
        # Copy img
        _, img_fname = os.path.split(img_fpath)
        img_fname = f"{i}_{img_fname}"  # prevents duplicate names
        shutil.copyfile(img_fpath, os.path.join(fdir_dst, img_fname))

        # Create annotations
        annotation_file = os.path.join(fdir_dst, img_fname.rsplit(".")[0] + ".txt")
        img_annotations: pd.DataFrame = yolo_annotations.loc[yolo_annotations["file_name"] == img_fpath, :]
        annotation_contents = []
        for i, line in img_annotations.iterrows():
            category = line["category_id"]
            bbox = line["yolo_bbox"]
            annotation_contents.append(ds_annotations.create_yolo_annotation_line(category, bbox) + "\n")
        with open(annotation_file, "w") as f:
            f.writelines(annotation_contents)
    print(f"Done converting TACO to YOLO. YOLO DS in: {fdir_dst}")


def cvt_yolo_box_to_relative_voc_dict(bbox: list) -> dict:
    """
    Converts to "relative" voc dict: x0, y0, x1, y2}
    :param bbox: [center_x_rel, center_y_rel, width_rel, height_rel]
    :return:
    """
    center_x_rel, center_y_rel, width_rel, height_rel = bbox
    bbox_out = [center_x_rel - 0.5 * width_rel, center_y_rel - 0.5 * height_rel,
                center_x_rel + 0.5 * width_rel, center_y_rel + 0.5 * height_rel]
    names = ["x0", "y0", "x1", "y1"]
    if np.any(np.array(bbox_out) < 0):
        raise bbox_conversions.BoxFormatError(f"Box contains negative coordinates: {bbox_out}")
    return {k: v for k, v in zip(names, bbox_out)}


def reproportion_yolo_ds(yolo_root_dir, target_dir, new_ratios: tuple, seed=42, exist_ok=False):
    # assert np.isclose(sum(new_ratios), 1)
    # pairs = get_yolo_img_annotation_pairs(yolo_root_dir)
    # target_dirs = create_yolo_directories(target_dir, exist_ok=exist_ok)
    # set_indices = ds_split.create_model_indices(len(pairs), *new_ratios)
    # print(set_indices)
    pass
    # ToDo Finish this


def recreate_labelme_set_from_yolo(yolo_ds_root, target_dir, exist_ok=False):
    """
    Merges annotations and images from the train-, validation- and test set into one folder, and recreates the labelme
    .json files.
    :param yolo_ds_root:
    :return:
    """
    # ToDo: Implement
    # ToDo: account for possibly missing materials_dict.json

    os.makedirs(target_dir, exist_ok=exist_ok)

    mats_dict_fpath = os.path.join(yolo_ds_root, "materials_dict.json")
    if os.path.exists(mats_dict_fpath):
        materials_dict = ds_annotations.load_materials_dict(mats_dict_fpath)
    else:
        materials_dict = ds_annotations.create_fallback_yolo_materials_dict(yolo_ds_root)
    print("Finding img/txt pairs...")
    img_txt_pairs = get_yolo_img_annotation_pairs(yolo_ds_root)
    pairs_count = len(img_txt_pairs)
    print("Rebuilding jsons...")
    for i, (fpath_img, fpath_txt) in enumerate(img_txt_pairs):
        if i % 50 == 0:
            print(f"{100 * i / pairs_count:.2f} % completed.")

        basename_img = os.path.splitext(os.path.split(fpath_img)[-1])[0]
        basename_txt = os.path.splitext(os.path.split(fpath_txt)[-1])[0]
        assert basename_img == basename_txt

        json_dst = f"{os.path.join(target_dir, basename_txt)}.json"
        logging.debug(f"Saving json as: {json_dst}")
        create_labelme_json_from_yolo(fpath_txt, fpath_img, include_img_data=False,
                                      materials_dict=materials_dict,
                                      save_dir=target_dir, overwrite=exist_ok)
        shutil.copyfile(fpath_img, os.path.join(target_dir, os.path.split(fpath_img)[-1]))
    print(f"Done. Recreated labelme dataset in: {target_dir}")


def cvt_coco_to_yolo(fpath_labels_json, fdir_dst=None, exist_ok=False):
    """

    :param fpath_labels_json: location of the
    :param fdir_dst:
    :return:
    """
    if fdir_dst is None:
        fdir_dst = os.path.split(fpath_labels_json)[0] + "/yolo_annotations"
    if not os.path.isdir(fdir_dst):
        os.makedirs(fdir_dst)
    if os.listdir(fdir_dst) and not exist_ok:
        raise FileExistsError(f"Target dir exists and is not empty: {fdir_dst}")


    imgs, annots = ds_annotations.load_coco_ds(fpath_labels_json)
    logging.debug(f"Img cols: {imgs.columns}")
    logging.debug(f"Annot cols: {annots.columns}")
    ds_merged = ds_annotations.merge_img_info_into_labels(imgs, annots)
    ds_merged_yolo = ds_annotations.cvt_df_coco_bbox_annotations_to_yolo(ds_merged)
    ds_merged_yolo_grouped = ds_merged_yolo.groupby("file_name")
    group_count = len(ds_merged_yolo_grouped)
    for i, (fname, group_df) in enumerate(ds_merged_yolo_grouped):
        group_df["yolo_line"] = group_df["category_id"].astype(str) + group_df["yolo_bbox"].astype(str)
        group_df["yolo_line"] = group_df["yolo_line"].str.replace("[", " ")
        group_df["yolo_line"] = group_df["yolo_line"].str.replace(",", "")
        group_df["yolo_line"] = group_df["yolo_line"].str.replace("]", "")

        yolo_lines = group_df["yolo_line"].tolist()
        yolo_lines = [e + "\n" for e in yolo_lines]

        fpath_annotation_file = os.path.join(fdir_dst, os.path.splitext(fname)[0] + ".txt")
        with open(fpath_annotation_file, "w") as f:
            f.writelines(yolo_lines)

        if (i + 1) % 25 == 0:
            print(f"Created yolo file for {i + 1} out of {group_count}")

    invalid_boxes = ds_annotations.get_invalid_yolo_boxes(fdir_dst, print_output=False)
    if invalid_boxes:
        print(f"Invalid yolo boxes in the following files:")
        for f in invalid_boxes:
            print(f)
    else:
        print("All yolo bboxes are valid.")
    print("Done.")


if __name__ == "__main__":
    loglevel = logging.DEBUG
    logformat = "[%(levelname)s]\t%(funcName)15s: %(message)s"
    logging.basicConfig(level=loglevel, format=logformat)
    # logging.disable()

    pd.options.display.width = 0


    # fdir_ds = "/media/findux/DATA/Documents/Malta_II/surveys/Messina/stereocam/frames/"
    # # materials_dict = ds_annotations.load_json("/media/findux/DATA/Documents/Malta_II/datasets/all_categories/materials.json")
    # materials_dict = ds_annotations.load_json("/media/findux/DATA/Documents/Malta_II/datasets/all_categories/materials.json")
    # create_yolo_dataset(fdir_src=fdir_ds, materials_dict=materials_dict,
    #                     fdir_dst="/home/findux/Desktop/stereoframes/")

    # ds_13 = "/media/findux/DATA/Documents/Malta_II/datasets/dataset_13_yolo/"
    # ds_13_dst = "/media/findux/DATA/Documents/Malta_II/datasets/dataset_13/"
    # recreate_labelme_set_from_yolo(yolo_ds_root=ds_13, target_dir=ds_13_dst)

    # ds_src = "/media/findux/DATA/Documents/Malta_II/datasets/all_categories/files/"
    # ds_dst = "/media/findux/DATA/Documents/Malta_II/datasets/dataset_17_yolo/"
    # create_yolo_annotations(ds_src, save_materials_dict=True)
    # mats_dict = ds_annotations.load_materials_dict("/media/findux/DATA/Documents/Malta_II/datasets/all_categories/materials.json")
    # create_yolo_dataset(fdir_src=ds_src, fdir_dst=ds_dst, materials_dict=mats_dict)

    # fpath_json = "/media/findux/DATA/Documents/Malta_II/datasets/UAVVASTE/UAVVaste/annotations/annotations.json"
    # cvt_coco_to_yolo(fpath_json, exist_ok=True)

    fdir_labelme = "/media/findux/DATA/Documents/Malta_II/datasets/all_categories/fix/"
    create_yolo_annotations(fdir_labelme, False)
