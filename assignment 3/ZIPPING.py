import numpy as np
first_list = []
second_list= []
imgs_house = ['house1.png'] * 5 + ['house2.png'] * 5 + ['house3.png'] * 5 + ['house4.png'] * 5 + ['house5.png'] * 5
imgs_face = ['face1.png'] * 5 + ['face2.png'] * 5 + ['face3.png'] * 5 + ['face4.png'] * 5 + ['face5.png'] * 5
Cues = ['Cue1'] * 50 + ['Cue2'] * 50

first_list.extend(imgs_face)
first_list.extend(imgs_house)
first_list.extend(imgs_face)
first_list.extend(imgs_house)
img_fs = ['face1.png', 'face2.png', 'face3.png', 'face4.png', 'face5.png'] * 5
img_hs = ['house1.png', 'house2.png', 'house3.png', 'house4.png', 'house5.png'] * 5

second_list.extend(img_hs)
second_list.extend(img_fs)
second_list.extend(img_hs)
second_list.extend(img_fs)
catimgs = list(zip(first_list, second_list, Cues))
np.random.shuffle(catimgs)
print(catimgs)


