# -*- coding: utf-8 -*-
# pip3 install numpy opencv-python

import json
import numpy as np
import cv2


#--- user define ---#

img_path = '----'
x_num_char = 50
y_num_char = 22

#-------------------#

# bash color code 2 rgb
colors = json.loads('[[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0], [0, 0, 128], [128, 0, 128], [0, 128, 128], [192, 192, 192], [128, 128, 128], [255, 0, 0], [0, 255, 0], [255, 255, 0], [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 95], [0, 0, 135], [0, 0, 175], [0, 0, 215], [0, 0, 255], [0, 95, 0], [0, 95, 95], [0, 95, 135], [0, 95, 175], [0, 95, 215], [0, 95, 255], [0, 135, 0], [0, 135, 95], [0, 135, 135], [0, 135, 175], [0, 135, 215], [0, 135, 255], [0, 175, 0], [0, 175, 95], [0, 175, 135], [0, 175, 175], [0, 175, 215], [0, 175, 255], [0, 215, 0], [0, 215, 95], [0, 215, 135], [0, 215, 175], [0, 215, 215], [0, 215, 255], [0, 255, 0], [0, 255, 95], [0, 255, 135], [0, 255, 175], [0, 255, 215], [0, 255, 255], [95, 0, 0], [95, 0, 95], [95, 0, 135], [95, 0, 175], [95, 0, 215], [95, 0, 255], [95, 95, 0], [95, 95, 95], [95, 95, 135], [95, 95, 175], [95, 95, 215], [95, 95, 255], [95, 135, 0], [95, 135, 95], [95, 135, 135], [95, 135, 175], [95, 135, 215], [95, 135, 255], [95, 175, 0], [95, 175, 95], [95, 175, 135], [95, 175, 175], [95, 175, 215], [95, 175, 255], [95, 215, 0], [95, 215, 95], [95, 215, 135], [95, 215, 175], [95, 215, 215], [95, 215, 255], [95, 255, 0], [95, 255, 95], [95, 255, 135], [95, 255, 175], [95, 255, 215], [95, 255, 255], [135, 0, 0], [135, 0, 95], [135, 0, 135], [135, 0, 175], [135, 0, 215], [135, 0, 255], [135, 95, 0], [135, 95, 95], [135, 95, 135], [135, 95, 175], [135, 95, 215], [135, 95, 255], [135, 135, 0], [135, 135, 95], [135, 135, 135], [135, 135, 175], [135, 135, 215], [135, 135, 255], [135, 175, 0], [135, 175, 95], [135, 175, 135], [135, 175, 175], [135, 175, 215], [135, 175, 255], [135, 215, 0], [135, 215, 95], [135, 215, 135], [135, 215, 175], [135, 215, 215], [135, 215, 255], [135, 255, 0], [135, 255, 95], [135, 255, 135], [135, 255, 175], [135, 255, 215], [135, 255, 255], [175, 0, 0], [175, 0, 95], [175, 0, 135], [175, 0, 175], [175, 0, 215], [175, 0, 255], [175, 95, 0], [175, 95, 95], [175, 95, 135], [175, 95, 175], [175, 95, 215], [175, 95, 255], [175, 135, 0], [175, 135, 95], [175, 135, 135], [175, 135, 175], [175, 135, 215], [175, 135, 255], [175, 175, 0], [175, 175, 95], [175, 175, 135], [175, 175, 175], [175, 175, 215], [175, 175, 255], [175, 215, 0], [175, 215, 95], [175, 215, 135], [175, 215, 175], [175, 215, 215], [175, 215, 255], [175, 255, 0], [175, 255, 95], [175, 255, 135], [175, 255, 175], [175, 255, 215], [175, 255, 255], [215, 0, 0], [215, 0, 95], [215, 0, 135], [215, 0, 175], [215, 0, 215], [215, 0, 255], [215, 95, 0], [215, 95, 95], [215, 95, 135], [215, 95, 175], [215, 95, 215], [215, 95, 255], [215, 135, 0], [215, 135, 95], [215, 135, 135], [215, 135, 175], [215, 135, 215], [215, 135, 255], [215, 175, 0], [215, 175, 95], [215, 175, 135], [215, 175, 175], [215, 175, 215], [215, 175, 255], [215, 215, 0], [215, 215, 95], [215, 215, 135], [215, 215, 175], [215, 215, 215], [215, 215, 255], [215, 255, 0], [215, 255, 95], [215, 255, 135], [215, 255, 175], [215, 255, 215], [215, 255, 255], [255, 0, 0], [255, 0, 95], [255, 0, 135], [255, 0, 175], [255, 0, 215], [255, 0, 255], [255, 95, 0], [255, 95, 95], [255, 95, 135], [255, 95, 175], [255, 95, 215], [255, 95, 255], [255, 135, 0], [255, 135, 95], [255, 135, 135], [255, 135, 175], [255, 135, 215], [255, 135, 255], [255, 175, 0], [255, 175, 95], [255, 175, 135], [255, 175, 175], [255, 175, 215], [255, 175, 255], [255, 215, 0], [255, 215, 95], [255, 215, 135], [255, 215, 175], [255, 215, 215], [255, 215, 255], [255, 255, 0], [255, 255, 95], [255, 255, 135], [255, 255, 175], [255, 255, 215], [255, 255, 255], [8, 8, 8], [18, 18, 18], [28, 28, 28], [38, 38, 38], [48, 48, 48], [58, 58, 58], [68, 68, 68], [78, 78, 78], [88, 88, 88], [98, 98, 98], [108, 108, 108], [118, 118, 118], [128, 128, 128], [138, 138, 138], [148, 148, 148], [158, 158, 158], [168, 168, 168], [178, 178, 178], [188, 188, 188], [198, 198, 198], [208, 208, 208], [218, 218, 218], [228, 228, 228], [238, 238, 238]]')

# load image & resize to nums of char
img = cv2.imread(img_path)
width = x_num_char
height = y_num_char
img = cv2.resize(img, (width, height)).reshape((-1, 3))

# get closest color code
res = np.zeros(len(img), dtype=np.int32)
for i in range(len(res)):
  res[i] = np.argmin(np.linalg.norm(colors - img[i], axis=1))
res = res.reshape((height, width))

# prepare
char_tplt = '\e[38;5;{i}m{text}\e[m'
class Counter:
  def __init__(self):
    self.counter = -1
  def next_char(self):
    self.counter += 1
    return 'ox+'[self.counter % 3]
ct = Counter()

# image to motd str
out = []
for line in res:
  this_line = []
  out.append(this_line)
  for color in line:
    this_line.append(char_tplt.format(i=color, text=ct.next_char()))
out_b = '\n'.join([''.join([cha for cha in line]) for line in out]) + '\n'

# 0x1b  --> ESC
out_b = out_b.encode().replace(b'\e', b'\x1b')

with open('motd', 'wb') as f:
  f.write(out_b)
