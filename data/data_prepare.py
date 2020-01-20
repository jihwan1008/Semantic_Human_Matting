import sys
import os
import cv2
import numpy as np

default_train = './aisegment/clip_img/'
default_mat = './aisegment/matting/'
txt_train = './train.txt'
txt_mat = './mask.txt'


tmp_dir = './image/'
if os.path.isdir(tmp_dir):
    pass
else:
    os.mkdir(tmp_dir)

file_1 = sorted(os.listdir(default_train))
#print(len(file_1))

tmp_list = []
tmp_list_ = []
print('Iterating through reference image directory architecture to get image file names...')
print('Generating Images folder...')
for item in file_1:
    file_2 = sorted(os.listdir(default_train + item))
    for elem in file_2:
        file_3 = sorted(os.listdir(default_train + item + '/' + elem))
        for blob in file_3:
            tmp_list.append(blob)
            img = cv2.imread(default_train + item + '/' + elem + '/' + blob)
            cv2.imwrite(tmp_dir + blob, img)

print('Total # of Ref images : {}'.format(len(tmp_list)))

with open(txt_train, 'w') as f:
    for item in tmp_list:
        f.write(item)
        f.write('\n')
    f.close()

del file_1
del file_2
del file_3
del tmp_dir

print('Iterating through matting image directory architecture to get matting file names...')
print('Generating Mask images...')

tmp_dir = './mask/'

if os.path.isdir(tmp_dir):
    pass
else:
    os.mkdir(tmp_dir)

file_1 = sorted(os.listdir(default_mat))
for item in file_1:
    file_2 = sorted(os.listdir(default_mat + item))
    for elem in file_2:
        file_3 = sorted(os.listdir(default_mat + item + '/' + elem))
        for blob in file_3:
            blob_ = blob[:-4] + '_mask' + '.png'
            tmp_list_.append(blob_)
            img = cv2.imread(default_mat + item + '/' + elem + '/' + blob)
            mask = np.full((img.shape[0], img.shape[1], img.shape[2]), 0, dtype=np.uint8)
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    if not (img[i,j,0] and img[i,j,1] and img[i,j,2]):
                        mask[i,j,0] = 255
                        mask[i,j,1] = 255
                        mask[i,j,2] = 255
            cv2.imwrite(tmp_dir + blob_, np.invert(mask))

print('Total # of Matting images : {}'.format(len(tmp_list_)))

with open(txt_mat, 'w') as f:
    for item in tmp_list_:
        f.write(item)
        f.write('\n')
    f.close()
