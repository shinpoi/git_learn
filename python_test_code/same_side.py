# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Q: https://math.stackexchange.com/questions/325141/probability-that-n-points-on-a-circle-are-in-one-semicircle

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
import sys

PI_2 = np.pi
PI_3 = np.pi
PI_4 = np.pi * 2

outputPlot = 1

# radius of circle
R = 1000
R2 = R ** 2

num_duck = 4

# num of samples
N = 10000


def gen_samples(n=5):
    samples = np.array(np.random.rand(n, num_duck, 2) * 2 * R - R, dtype=np.float64)
    for i in range(n):
        if i % 10000 == 0:
            print('%d/%d' % (i, n))
        for d in range(num_duck):
            x, y = samples[i][d]
            # regenerate when out of circle
            while (x ** 2 + y ** 2 >= R2):
                samples[i][d] = np.random.rand(2) * 2 * R - R
                x, y = samples[i][d]
    return samples


# get radian of line (0,0) -> (x,y)
def get_radians(xylist):
    slops = np.array([y / x for x, y in xylist], dtype=np.float64)
    radians = np.arctan(slops)
    for i in range(len(xylist)):
        x, y = xylist[i]
        if (x > 0) and (y > 0):
            continue
        elif (x < 0) and (y > 0):
            radians[i] += PI_2
        elif (x < 0) and (y < 0):
            radians[i] += PI_3
        else:
            radians[i] += PI_4
    return radians


def is_same_side(li):
    tmp = li[0]
    ref = -1
    for i in range(len(li)):
        now = li[i]
        if all([(x - now) % PI_4 < np.pi for x in li]):
            ref = i
            break
    return ref


def _assert_any(_except, _actual, name=''):
    if any(_except != _actual):
        print('except %s = %s, but get %s' % (name, str(_except), str(_actual)))


def _assert(_except, _actual, name=''):
    if _except != _actual:
        print('except %s = %s, but get %s' % (name, str(_except), str(_actual)))


def test():
    _assert_any([np.pi / 4, np.pi / 2 + np.pi / 4, np.pi + np.pi / 4, np.pi * 3 / 2 + np.pi / 4],
                get_radians([(1, 1), (-1, 1), (-1, -1), (1, -1)]),
                'radian'
                )

    # same quarter
    xyli = get_radians([(1, 1), (2, 1), (1, 2), (3, 1)])
    _assert(True, is_same_side(xyli), 'is_same_side %s' % str(xyli))

    # same side
    xyli = get_radians([(2, 1), (1, 2), (-1, 2), (-2, 1)])
    _assert(True, is_same_side(xyli), 'is_same_side %s' % str(xyli))

    # same side (minus)
    xyli = get_radians([(1, 1), (2, 1), (1, -2), (3, -1)])
    _assert(True, is_same_side(xyli), 'is_same_side %s' % str(xyli))

    # three quarter but same side
    xyli = get_radians([(100, 1), (-1, -200), (-1, -1), (-2, -3)])
    _assert(True, is_same_side(xyli), 'is_same_side %s' % str(xyli))

    # not same side
    xyli = get_radians([(1, 1), (-1, 1), (-1, -1), (1, -1)])
    _assert(False, is_same_side(xyli), 'is_same_side %s' % str(xyli))


if __name__ == '__main__':
    # test()
    # np.set_printoptions(suppress=True)
    # print(gen_samples(50))
    ducks = gen_samples(N).reshape(N * num_duck, 2)
    radians = get_radians(ducks).reshape(N, num_duck)
    print('start check ducks')
    is_same_side_list = [is_same_side(duck) for duck in radians]
    res = len([x for x in is_same_side_list if x >= 0])
    print('same side: %d (%f%%)' % (res, res * 100 / N))

    if not outputPlot:
        sys.exit(0)

    ducks.resize((N, num_duck, 2))
    date = datetime.now().strftime("%H%M%S")
    os.makedirs('res/' + date + '_yesyes')
    os.makedirs('res/' + date + '_nono')
    for i in range(N):
        ref = is_same_side_list[i]
        if ref >= 0:
            surffix = 'yesyes'
        else:
            surffix = 'nono'
        degree = ducks[i][ref][1] / ducks[i][ref][0]
        split_x = np.arange(-1 * R, R, R / 10, dtype=np.float64)
        split_y = split_x * degree
        fig = plt.figure(figsize=(6, 6))
        circle = plt.Circle((0, 0), R, color='b', fill=False)
        ax = plt.gca()
        ax.cla()
        ax.set_xlim((-1 * R, R))
        ax.set_ylim((-1 * R, R))
        duck = ducks[i]
        # ax.plot((0,), (0,), '.', color="blue", linewidth=5)
        ax.plot(split_x, split_y, color="blue", linewidth=1)
        ax.plot(duck[:, 0], duck[:, 1], '.', color="red", linewidth=10)
        ax.add_artist(circle)
        fig.savefig('res/%s_%s/%d.png' % (date, surffix, i))
        plt.close()
