import os
import cv2
output_dir='./clf-data/all'
mask_path='./mask_1920_1080.png'
mask=cv2.imread(mask_path,0)

analysis=cv2.connectedComponentsWithStats(mask,4,cv2.)