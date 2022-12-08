import shutil
import random
import math
import numpy as np

root_dir = 'Project/base'
classes = ['neg']

for clss in classes:
    print('------------' + clss + '-------------')
    dirtry = root_dir + '/' + clss
    print(dirtry)
    files = os.listdir(dirtry)
    np.random.shuffle(files)

    base_outdir = 'Project/'
    print(len(files))

    for folder in ['train', 'val', 'test']:
        target_dir = base_outdir + folder
        target_class = target_dir + '/' + clss
        if folder == 'train':
            print('------------' + folder + '-------------')
            images_to_pass = files[: math.floor(0.6*len(files))]
            print(math.floor(0.6*len(files)))
            for img in images_to_pass:
                img = dirtry + '/' + img
                shutil.copy(img, target_class)
        elif folder == 'val':
            print('------------' + folder + '-------------')
            images_to_pass = files[math.floor(0.6*len(files)): math.floor(0.8*len(files))]
            print(math.floor(0.8*len(files))-math.floor(0.6*len(files)))
            for img in images_to_pass:
                img = dirtry + '/' + img
                shutil.copy(img, target_class)
        else:
            print('------------' + folder + '-------------')
            images_to_pass = files[math.floor(0.8*len(files)):]
            print(64833-math.floor(0.8*len(files)))
            for img in images_to_pass:
                img = dirtry + '/' + img
                shutil.copy(img, target_class)
