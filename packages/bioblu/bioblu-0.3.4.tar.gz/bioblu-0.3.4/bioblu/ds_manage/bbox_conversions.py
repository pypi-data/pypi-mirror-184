#!/usr/bin/env python3

import logging
import numpy as np
from typing import List, Union


FORMATS = {"coco": "[x0, y0, w, h] (absolute)",
           "labelme": "[[corner_0_x, corner_0_y], [corner_1_x, corner_1_y]] (absolute)",
           "voc": "[x0, y0, x1, y1] (absolute)",
           "yolo": "[cx, cy, w, h] (relative)"}


class BoxFormatError(Exception):
    def __init__(self, error_message=None):
        if error_message is None:
            error_message = "Wrong BBox format."
        super().__init__(error_message)


def yolo_bbox_is_within_bounds(bbox: List[float]) -> bool:
    if all(0 <= np.array(bbox)) and all(np.array(bbox) <= 1):
        return True
    else:
        return False


def confirm_yolo_bbox_bounds(bbox: List) -> None:
    if not yolo_bbox_is_within_bounds(bbox):
        print(f"Yolo bbox out of bounds: {bbox}")
        raise BoxFormatError


def set_negative_to_zero(x_in: list):
    """
    Sets negative elements in the list to zero. Returns the updated list. Accepts nested lists.
    :param x_in:
    :return:
    """
    list_out = []
    for e in x_in:
        if isinstance(e, list):
            list_out.append(set_negative_to_zero(e))
        else:
            if e < 0:
                list_out.append(0)
            else:
                list_out.append(e)
    # list_out = [0 if e < 0 else e for e in x_in]
    return list_out


# ToDo: refactor these as xyxy, xywh, cxrcyrwrhr or x_y_x_y, xcr_ycr_wr_hr x_y_w_h

def fix_labelme_point_order(labelme_bbox: List[List[float]]) -> List[List[float]]:
    """
    Converts [[any_x, any_y], [any_x, any_y]] to [[x0, y0], [x1, y1]]
    """
    labelme_bbox = set_negative_to_zero(labelme_bbox)
    [x0, y0], [x1, y1] = labelme_bbox
    xvals = [x0, x1]
    yvals = [y0, y1]
    return [[np.min(xvals), np.min(yvals)], [np.max(xvals), np.max(yvals)]]


def coco_to_labelme(coco_bbox: List[int]) -> List[List[int]]:
    """
    Converts  [x0, y0, w, h] to [[TLx, TLy], [BRx, BRy]]
    :param coco_bbox:
    :return:
    """
    if not np.all(np.array(coco_bbox) >= 0):
        print(f"Setting negative bbox coordinates to zero: {coco_bbox}")
        coco_bbox = set_negative_to_zero(coco_bbox)
    x1, y1, x2, y2 = coco_to_voc(coco_bbox)
    out = [[x1, y1], [x2, y2]]
    assert np.all(np.array(out) >= 0)
    return out


def coco_to_voc(coco_bbox: List[int]):
    """Converts [x0, y0, w, h] to [x0, y0, x1, y1]"""
    logging.debug(coco_bbox)
    if not np.all(np.array(coco_bbox) >= 0):
        print(f"Setting negative bbox coordinates to zero: {coco_bbox}")
        coco_bbox = set_negative_to_zero(coco_bbox)
    x, y, w, h = coco_bbox
    return [x, y, x + w - 1, y + h - 1]  # - 1 because of zero indexing of pixels, because dimensions start at 1.


def coco_to_yolo(coco_bbox: List[int], img_width: int, img_height: int):
    """Converts [x0, y0, w, h] to [xc_rel, yc_rel, w_rel, h_rel]"""
    if not np.all(np.array(coco_bbox) >= 0):
        print(f"Setting negative bbox coordinates to zero: {coco_bbox}")
        coco_bbox = set_negative_to_zero(coco_bbox)

    bbox_x, bbox_y, bbox_w, bbox_h = coco_bbox

    bbox_center_x_abs = bbox_x + 0.5 * bbox_w
    bbox_center_x_rel = bbox_center_x_abs / img_width
    bbox_center_y_abs = bbox_y + 0.5 * bbox_h
    bbox_center_y_rel = bbox_center_y_abs / img_height

    bbox_width_rel = bbox_w / img_width
    bbox_height_rel = bbox_h / img_height

    yolo_bbox = [bbox_center_x_rel, bbox_center_y_rel, bbox_width_rel, bbox_height_rel]

    try:
        confirm_yolo_bbox_bounds(yolo_bbox)
    except BoxFormatError:
        print(f"Warning: using invalid yolo bbox: {yolo_bbox}")

    return yolo_bbox


def labelme_to_yolo(labelme_bbox: List[List[float]], img_width: int, img_height: int):
    """Converts [[x0, y0], [x1, y1]] to [xc_rel, yc_rel, w_rel, h_rel]"""
    if not all(np.array(labelme_bbox).flatten() >= 0):
        print(f"Setting negative labelme bbox coordinates to zero: {labelme_bbox}")
        labelme_bbox = set_negative_to_zero(labelme_bbox)
    labelme_bbox = list(fix_labelme_point_order(labelme_bbox))
    _voc_box = list(np.array(labelme_bbox).flatten())
    _coco = voc_to_coco(_voc_box)
    yolo_bbox = coco_to_yolo(_coco, img_width=img_width, img_height=img_height)
    return yolo_bbox


def labelme_to_voc(labelme_bbox):
    """Converts [[x0, y0], [x1, y1]] to [x0, y0, x1, y1]"""
    if not all(np.array(labelme_bbox).flatten() >= 0):
        print(f"Setting negative labelme bbox coordinates to zero: {labelme_bbox}")
        labelme_bbox = set_negative_to_zero(labelme_bbox)
    _points_fixed = fix_labelme_point_order(labelme_bbox)
    _points_ints = np.round(np.array(_points_fixed)).astype(int)
    return list(_points_ints.flatten())


def labelme_to_coco(labelme_bbox):
    """Converts [[x0, y0], [x1, y1]] to [x0, y0, w, h]"""
    if not all(np.array(labelme_bbox).flatten() >= 0):
        print(f"Setting negative labelme bbox coordinates to zero: {labelme_bbox}")
        labelme_bbox = set_negative_to_zero(labelme_bbox)
    _points_fixed = fix_labelme_point_order(labelme_bbox)
    x0, y0, x1, y1 = np.array(_points_fixed).flatten()
    box_width = x1 - x0 + 1  # +1 because dims are not zero-indexed
    box_height = y1 - y0 + 1  # ditto
    return [x0, y1, box_width, box_height]


def voc_to_yolo(voc_bbox, img_width, img_height):
    """Converts [x0, y0, x1, y1] to [xc_rel, yc_rel, w_rel, h_rel]"""
    if not all(np.array(voc_bbox).flatten() >= 0):
        print(f"Setting negative voc bbox coordinates to zero: {voc_bbox}")
        voc_bbox = set_negative_to_zero(voc_bbox)
    _coco = voc_to_coco(voc_bbox)
    yolo = coco_to_yolo(_coco, img_width, img_height)
    return yolo


def voc_to_coco(voc_bbox: list):
    """Converts [x0, y0, x1, y1] to [x0, y0, w, h]"""
    if not all(np.array(voc_bbox).flatten() >= 0):
        print(f"Setting negative voc bbox coordinates to zero: {voc_bbox}")
        voc_bbox = set_negative_to_zero(voc_bbox)
    x0, y0, x1, y1 = voc_bbox
    w = int((x1 + 1) - x0)
    h = int((y1 + 1) - y0)
    return [x0, y0, w, h]


def voc_to_labelme(voc_bbox):
    """Converts [x0, y0, x1, y1] to [[x0, y0], [x1, y1]]"""
    if not all(np.array(voc_bbox).flatten() >= 0):
        print(f"Setting negative voc bbox coordinates to zero: {voc_bbox}")
        voc_bbox = set_negative_to_zero(voc_bbox)
    x0, y0, x1, y1 = voc_bbox
    return [[x0, y0], [x1, y1]]


def yolo_to_coco(yolo_bbox, img_width: int, img_height: int):
    """Converts [xc_rel, yc_rel, w_rel, h_rel] to [x0, y0, w, h]"""

    if not all(np.array(yolo_bbox).flatten() >= 0):
        print(f"Setting negative yolo bbox coordinates to zero: {yolo_bbox}")
        yolo_bbox = set_negative_to_zero(yolo_bbox)

    assert np.all(0 <= np.array(yolo_bbox))
    assert np.all(1 >= np.array(yolo_bbox))
    assert np.all(np.array([img_width, img_height]) > 0)
    center_x_norm, center_y_norm, width_norm, height_norm = yolo_bbox
    coco_x = int(np.round((center_x_norm - 0.5 * width_norm) * img_width))
    coco_y = int(np.round((center_y_norm - 0.5 * height_norm) * img_height))

    if coco_x < 0:
        coco_x = 0
    if coco_y < 0:
        coco_y = 0

    coco_boxwidth = int(np.round(width_norm * img_width))
    coco_boxheight = int(np.round(height_norm * img_height))
    return [coco_x, coco_y, coco_boxwidth, coco_boxheight]


def yolo_to_voc(yolo_bbox, img_width, img_height):
    """Converts [xc_rel, yc_rel, w_rel, h_rel] to [x0, y0, x1, y1]"""

    if not all(np.array(yolo_bbox).flatten() >= 0):
        print(f"Setting negative yolo bbox coordinates to zero: {yolo_bbox}")
        yolo_bbox = set_negative_to_zero(yolo_bbox)

    _coco = yolo_to_coco(yolo_bbox, img_width, img_height)
    voc = coco_to_voc(_coco)
    return voc


def yolo_to_labelme(yolo_bbox: List[float], img_width: int, img_height: int) -> List[List[int]]:
    """Converts [xc_rel, yc_rel, w_rel, h_rel] to [[x0, y0], [x1, y1]]"""

    if not all(np.array(yolo_bbox).flatten() >= 0):
        print(f"Setting negative yolo bbox coordinates to zero: {yolo_bbox}")
        yolo_bbox = set_negative_to_zero(yolo_bbox)

    _voc = yolo_to_voc(yolo_bbox, img_width, img_height)
    x0, y0, x1, y1 = _voc
    return [[x0, y0], [x1, y1]]


def convert_bbox_coco_to_yolo_bbox(coco_bbox: list, img_width: int, img_height: int):
    """
    DEPRECATED.
    Use bbox_conversions module instead.

    Converts a bbox list from coco to yolo format
    :param coco_bbox:
    :param img_width:
    :param img_height:
    :return:
    """
    if not all(np.array(coco_bbox).flatten() >= 0):
        print(f"Setting negative coco bbox coordinates to zero: {coco_bbox}")
        coco_bbox = set_negative_to_zero(coco_bbox)

    _bbox_x, _bbox_y, _bbox_width, _bbox_height = coco_bbox
    bbox_center_x_normalised = (_bbox_x + 0.5 * _bbox_width) / img_width
    bbox_center_y_normalised = (_bbox_y + 0.5 * _bbox_height) / img_height
    bbox_width_normalised = (_bbox_width / img_width)
    bbox_height_normalised = (_bbox_height / img_height)
    bbox_out = [bbox_center_x_normalised, bbox_center_y_normalised, bbox_width_normalised, bbox_height_normalised]
    if np.any(np.array(bbox_out) < 0):
        raise BoxFormatError(f"Box contains negative coordinates: {bbox_out}")
    return bbox_out


def test_coco(coco_bbox, img_width, img_height):
    print(f"Original box: {coco_bbox} | Img width: {img_width} | Img height: {img_height}")
    print(f'COCO: {coco_bbox} (original)')
    yolo_box = coco_to_yolo(coco_bbox, img_width, img_height)
    print(f'YOLO: {yolo_box} (from COCO)')
    coco_from_yolo = yolo_to_coco(yolo_box, img_width, img_height)
    print(f'COCO: {coco_from_yolo} (from YOLO)')
    voc_from_coco = coco_to_voc(coco_bbox)
    print(f'VOC: {voc_from_coco} (from COCO)')
    voc_from_yolo = yolo_to_voc(yolo_box, img_width, img_height)
    print(f'VOC: {voc_from_yolo} (from YOLO)')
    coco_from_voc = voc_to_coco(voc_from_yolo)
    print(f'COCO: {coco_from_voc} (from VOC)')
    print()


def test_labelme(labelme_bbox, img_width, img_height):
    voc = labelme_to_voc(labelme_bbox)
    print(f'VOC:\t{voc}')
    yolo = labelme_to_yolo(labelme_bbox, img_width, img_height)
    print(f'YOLO: \t{yolo}')


if __name__ == "__main__":

    # print(yolo_to_coco([0.765625, 0.051125, 0.43146929824561403, 0.10275], 1824, 4000))
    print(set_negative_to_zero([3, 0, -0.5]))
    print(set_negative_to_zero([[3, 0], [-0.5, 3], 5, 0, -1]))