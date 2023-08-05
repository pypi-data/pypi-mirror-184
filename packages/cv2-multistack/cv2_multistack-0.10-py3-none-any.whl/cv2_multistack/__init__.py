import cv2
import numpy as np
from a_cv_imwrite_imread_plus import open_image_in_cv


def get_new_relative_size_from_width(img, width=100):
    ratio = img.shape[0] / img.shape[1]
    height = width * ratio
    dim = (int(width), int(height))
    return dim


def get_new_relative_size_from_height(img, height=100):
    ratio = img.shape[1] / img.shape[0]
    width = height * ratio
    dim = (int(width), int(height))
    return dim


def cv2resize(image, dim, interpolation=cv2.INTER_AREA):
    return cv2.resize(image.copy(), dim, interpolation=interpolation)


def cv2_resize_fixed_width(img, width=100):
    dim = get_new_relative_size_from_width(img, width=width)
    bia1 = cv2resize(img, dim)
    return bia1


def cv2_resize_fixed_height(img, height=100):
    dim = get_new_relative_size_from_height(img, height=height)
    bia1 = cv2resize(img, dim)
    return bia1


def vstack_multiple_pics(listofpics, width=100, channels=3):
    allpi = []
    for img1 in listofpics:
        allpi.append(cv2_resize_fixed_width(open_image_in_cv(img1,channels_in_output=channels), width=width))
    return np.vstack(allpi)


def hstack_multiple_pics(listofpics, height=100, channels=3):
    allpi = []
    for img1 in listofpics:
        allpi.append(cv2_resize_fixed_height(open_image_in_cv(img1,channels_in_output=channels), height=height))
    return np.hstack(allpi)
