import time
import curses
import random
import copy

H = 35
W = 100
RANDOM_LIVE = 0.001
EPOCH = 100
SLEEP = 1

# ○●⊙ ◇◆ □■ ★☆
LIVE_CHAR = '●'
DIE_CHAR = ' '

rangeH = tuple([i for i in range(1, H-1)])
rangeW = tuple([i for i in range(1, W-1)])
DOT_ARR_TEMPLATE = []


class Dot(object):
    # s: set, chain: num of chain
    def __init__(self):
        self.live = False
        self.s = set()
        self.chain = 0


def get_next_str(now_arr):
    # now_arr.shape = (h, w)
    next_arr = get_next_arr(now_arr)
    next_str_arr = []
    for row in next_arr:
        li = [LIVE_CHAR if dot.live else DIE_CHAR for dot in row]
        li.append('\n')
        next_str_arr.append(li)
    return next_arr, ''.join([''.join(li) for li in next_str_arr])


# set next status by chain number
def get_next_arr(now_arr):
    next_arr = copy.deepcopy(DOT_ARR_TEMPLATE)
    calc_status(now_arr)
    for x in rangeH:
        for y in rangeW:
            dot = now_arr[x][y]
            next_dot = next_arr[x][y]
            # 2, 3: live, other: die
            if dot.live:
                if dot.chain == 3 or dot.chain == 4:
                    next_dot.live = True
                elif int(random.random() + RANDOM_LIVE):
                    next_dot.live = True
            else:
                if dot.chain == 2:
                    next_dot.live = True
                elif int(random.random() + RANDOM_LIVE):
                    next_dot.live = True
    return next_arr


# calc num of chain
def calc_status(now_arr):
    # calc set
    for x in rangeH:
        for y in rangeW:
            dot = now_arr[x][y]
            # live - near: 0: new set, 1: add in set, 2: union and add in set
            if dot.live:
                up_set = now_arr[x-1][y].s
                left_set = now_arr[x][y-1].s
                if len(up_set) == len(left_set) == 0:
                    dot.s = set()
                    dot.s.add(dot)
                if len(up_set) > 0 and len(left_set) > 0:
                    if up_set is left_set:
                        up_set.add(dot)
                        dot.s = up_set
                    else:
                        union_set = up_set.union(left_set)
                        union_set.add(dot)
                        for dot_ in union_set:
                            dot_.s = union_set
                if len(up_set) > 0:
                    up_set.add(dot)
                    dot.s = up_set
                if len(left_set) > 0:
                    left_set.add(dot)
                    dot.s = left_set
    # calc length
    for x in rangeH:
        for y in rangeW:
            dot = now_arr[x][y]
            if dot.live:
                # live dot:
                dot.chain = len(dot.s)
            else:
                # died dot:
                dot.chain = len(now_arr[x-1][y].s) +\
                            len(now_arr[x+1][y].s) +\
                            len(now_arr[x][y-1].s) +\
                            len(now_arr[x][y+1].s)


# to terminal
def pbar(window):
    window.scrollok(True)
    window.clearok(True)
    now_arr = init_arr()
    for i in range(EPOCH):
        now_arr, now_str = get_next_str(now_arr)
        now_str = ("epoch: %s\n========================\n" % i) + now_str
        window.clear()
        window.addstr(now_str)
        window.refresh()
        time.sleep(SLEEP)


# just for test
def print2terminal():
    now_arr = init_arr()
    for i in range(EPOCH):
        now_arr, now_str = get_next_str(now_arr)
        print("epoch: %s\n========================\n" % i)
        print(now_str)
        time.sleep(SLEEP)


def init_arr():
    # init DOT_ARR_TEMPLATE
    for x in range(H):
        DOT_ARR_TEMPLATE.append([])
        for y in range(W):
            DOT_ARR_TEMPLATE[x].append(Dot())

    # init first arr
    now_arr = copy.deepcopy(DOT_ARR_TEMPLATE)
    for x in rangeH:
        for y in rangeW:
            if int(random.random() + 0.1):
                now_arr[x][y].live = True

    return now_arr

 
if __name__ == '__main__':
    curses.wrapper(pbar)
    # print2terminal()
