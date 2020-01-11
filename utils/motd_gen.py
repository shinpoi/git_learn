# -*- coding: utf-8 -*-
# Image to 256 color motd (by background color)
# pip3 install numpy opencv-python

import numpy as np
import cv2
import sys
from random import randint,choice

#--- user define ---#
base_path = '.'
default_x_len = 40
default_y_len = 16

# 0 ~ 255, pixel will be transparent if alpha big than this 
alpha_threshold = 10

# params: filename, [width, height]
width = default_x_len
height = default_y_len

if len(sys.argv) > 1:
  img_path = base_path + '/' + sys.argv[1]
if len(sys.argv) > 3:
  width = int(sys.argv[2])
  height = int(sys.argv[3])
 
#-------------------#

# bash color code 2 rgb (index: bash color code; value: rgb)
# > https://jonasjacek.github.io/colors/
colors = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0], [0, 0, 128], [128, 0, 128], [0, 128, 128], [192, 192, 192], [128, 128, 128], [255, 0, 0], [0, 255, 0], [255, 255, 0], [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 95], [0, 0, 135], [0, 0, 175], [0, 0, 215], [0, 0, 255], [0, 95, 0], [0, 95, 95], [0, 95, 135], [0, 95, 175], [0, 95, 215], [0, 95, 255], [0, 135, 0], [0, 135, 95], [0, 135, 135], [0, 135, 175], [0, 135, 215], [0, 135, 255], [0, 175, 0], [0, 175, 95], [0, 175, 135], [0, 175, 175], [0, 175, 215], [0, 175, 255], [0, 215, 0], [0, 215, 95], [0, 215, 135], [0, 215, 175], [0, 215, 215], [0, 215, 255], [0, 255, 0], [0, 255, 95], [0, 255, 135], [0, 255, 175], [0, 255, 215], [0, 255, 255], [95, 0, 0], [95, 0, 95], [95, 0, 135], [95, 0, 175], [95, 0, 215], [95, 0, 255], [95, 95, 0], [95, 95, 95], [95, 95, 135], [95, 95, 175], [95, 95, 215], [95, 95, 255], [95, 135, 0], [95, 135, 95], [95, 135, 135], [95, 135, 175], [95, 135, 215], [95, 135, 255], [95, 175, 0], [95, 175, 95], [95, 175, 135], [95, 175, 175], [95, 175, 215], [95, 175, 255], [95, 215, 0], [95, 215, 95], [95, 215, 135], [95, 215, 175], [95, 215, 215], [95, 215, 255], [95, 255, 0], [95, 255, 95], [95, 255, 135], [95, 255, 175], [95, 255, 215], [95, 255, 255], [135, 0, 0], [135, 0, 95], [135, 0, 135], [135, 0, 175], [135, 0, 215], [135, 0, 255], [135, 95, 0], [135, 95, 95], [135, 95, 135], [135, 95, 175], [135, 95, 215], [135, 95, 255], [135, 135, 0], [135, 135, 95], [135, 135, 135], [135, 135, 175], [135, 135, 215], [135, 135, 255], [135, 175, 0], [135, 175, 95], [135, 175, 135], [135, 175, 175], [135, 175, 215], [135, 175, 255], [135, 215, 0], [135, 215, 95], [135, 215, 135], [135, 215, 175], [135, 215, 215], [135, 215, 255], [135, 255, 0], [135, 255, 95], [135, 255, 135], [135, 255, 175], [135, 255, 215], [135, 255, 255], [175, 0, 0], [175, 0, 95], [175, 0, 135], [175, 0, 175], [175, 0, 215], [175, 0, 255], [175, 95, 0], [175, 95, 95], [175, 95, 135], [175, 95, 175], [175, 95, 215], [175, 95, 255], [175, 135, 0], [175, 135, 95], [175, 135, 135], [175, 135, 175], [175, 135, 215], [175, 135, 255], [175, 175, 0], [175, 175, 95], [175, 175, 135], [175, 175, 175], [175, 175, 215], [175, 175, 255], [175, 215, 0], [175, 215, 95], [175, 215, 135], [175, 215, 175], [175, 215, 215], [175, 215, 255], [175, 255, 0], [175, 255, 95], [175, 255, 135], [175, 255, 175], [175, 255, 215], [175, 255, 255], [215, 0, 0], [215, 0, 95], [215, 0, 135], [215, 0, 175], [215, 0, 215], [215, 0, 255], [215, 95, 0], [215, 95, 95], [215, 95, 135], [215, 95, 175], [215, 95, 215], [215, 95, 255], [215, 135, 0], [215, 135, 95], [215, 135, 135], [215, 135, 175], [215, 135, 215], [215, 135, 255], [215, 175, 0], [215, 175, 95], [215, 175, 135], [215, 175, 175], [215, 175, 215], [215, 175, 255], [215, 215, 0], [215, 215, 95], [215, 215, 135], [215, 215, 175], [215, 215, 215], [215, 215, 255], [215, 255, 0], [215, 255, 95], [215, 255, 135], [215, 255, 175], [215, 255, 215], [215, 255, 255], [255, 0, 0], [255, 0, 95], [255, 0, 135], [255, 0, 175], [255, 0, 215], [255, 0, 255], [255, 95, 0], [255, 95, 95], [255, 95, 135], [255, 95, 175], [255, 95, 215], [255, 95, 255], [255, 135, 0], [255, 135, 95], [255, 135, 135], [255, 135, 175], [255, 135, 215], [255, 135, 255], [255, 175, 0], [255, 175, 95], [255, 175, 135], [255, 175, 175], [255, 175, 215], [255, 175, 255], [255, 215, 0], [255, 215, 95], [255, 215, 135], [255, 215, 175], [255, 215, 215], [255, 215, 255], [255, 255, 0], [255, 255, 95], [255, 255, 135], [255, 255, 175], [255, 255, 215], [255, 255, 255], [8, 8, 8], [18, 18, 18], [28, 28, 28], [38, 38, 38], [48, 48, 48], [58, 58, 58], [68, 68, 68], [78, 78, 78], [88, 88, 88], [98, 98, 98], [108, 108, 108], [118, 118, 118], [128, 128, 128], [138, 138, 138], [148, 148, 148], [158, 158, 158], [168, 168, 168], [178, 178, 178], [188, 188, 188], [198, 198, 198], [208, 208, 208], [218, 218, 218], [228, 228, 228], [238, 238, 238]]
colors = np.array(colors, dtype=np.int32)

# load image & resize
print('read: ' + img_path)
img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

print('read image as: %s, resize to: %s' % (str(img.shape), str((width, height))))
img = cv2.resize(img, (width, height), interpolation=cv2.INTER_NEAREST)

if img.shape[2] is 4:
  alpha = img[:,:,3].reshape((img.shape[0] * img.shape[1],))
  img = img[:,:,:3]
else:
  print('[warning] not found aplaha channel')
  alpha = np.ones((img.shape[0] * img.shape[1], ), dtype=np.int32)*255


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).reshape((-1, 3))

# calc closest color code
res = np.zeros(len(img), dtype=np.int32)
for i in range(len(res)):
  # humna perception color difference: https://en.wikipedia.org/wiki/Color_difference
  rmeans = (colors[:, 0] + img[i, 0]) / 2
  _delta = colors - img[i] 
  delta = np.sqrt((2 + rmeans/256) * _delta[:,0]**2 + 4 * _delta[:,1]**2 + (2 + (255 - rmeans)/256)*_delta[:,2]**2)
  res[i] = np.argmin(delta)
res = res.reshape((height, width))


'''
# remove background by color
img.resize((height, width, 3))
for y in range(img.shape[0]):
  for x in range(img.shape[1]):
    if np.sum(img[y, x]) > 250*3:  # remove white background
    # if np.sum(img[y, x]) < 10:     # remove black background
      res[y, x] = -1

# use ascii char
# char_tplt = '\e[38;5;{i}m{text}\e[m'  # char color
char_tplt = '\e[48;5;{i}m{text}\e[m'  # background color
char_list = [i for i in range(0x5B, 0x7C)] + [i for i in range(0x21, 0x41)]
class Counter:
  def __init__(self):
    self.counter = -1
    self.s = 'x+o'
  def next_char(self):
    self.counter += 1
    return chr(choice(char_list))
    # return self.s[self.counter % (len(self.s))]
ct = Counter()
'''

# image to motd
char_tplt = '\e[48;5;{i}m{text}\e[m'  # background color
out = []
n_px = -1
for line in res:
  this_line = []
  out.append(this_line)
  for color in line:
    n_px += 1
    if alpha[n_px] < alpha_threshold:
      this_line.append('　')
    else:
      this_line.append(char_tplt.format(i=color, text='　'))
out_b = '\n'.join([''.join([cha for cha in line]) for line in out]) + '\n'

# 0x1b  --> ESC
out_b = out_b.encode().replace(b'\e', b'\x1b')

# write to ./motd
with open('motd', 'wb') as f:
  f.write(out_b)

# confirm (print to console)
import sys
print('')
sys.stdout.buffer.write(out_b)
