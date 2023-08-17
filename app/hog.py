import cv2
import numpy as np

def getHog_descriptors(img):
    new_image = cv2.resize(img,(128,128),interpolation=cv2.INTER_AREA)
    win_size = new_image.shape
    cell_size = (8, 8)
    block_size = (16, 16)
    block_stride = (8, 8)
    num_bins = 9

    hog = cv2.HOGDescriptor(win_size, block_size, block_stride,cell_size, num_bins)

    hog_descriptor = hog.compute(new_image)
    return hog_descriptor
