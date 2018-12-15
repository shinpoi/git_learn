import numpy as np
import matplotlib.pyplot as plt
from hashlib import md5

STR = "Now Humbert is of course very cruel to Lolita, not just in the ruthless sine qua non of her subjugation, " \
      "nor yet in his sighing intention of 'somehow' getting rid of her when her brief optimum has elapsed, " \
      "nor yet in his fastidious observation of signs of wear in his 'frigid' and 'ageing mistress'. " \
      "Humbert is surpassingly cruel in using Lolita for the play of his wit and the play of his prose-his prose, " \
      "which sometimes resembles the 'sweat-drenched finery' that 'a brute of forty' may casually and legally shed " \
      "(in both hemispheres, as a scandalized Humbert notes) before thrusting " \
      "'himself up to the hilt into his youthful bride'. Morally the novel is all ricochet or rebound. " \
      "However cruel Humbert is to Lolita, Nabokov is crueller to Humbert-finessingly cruel. " \
      "We all share the narrator's smirk when he begins the sexual-bribes chapter with the following sentence: " \
      "'I am now faced with the distasteful task of recording a definite drop in Lolita's morals.' " \
      "But when the smirk congeals we are left staring at the moral heap that Humbert has become, " \
      "underneath his arched eyebrow. Irresistible and unforgivable. It is complicated, and unreassuring. " \
      "Even so, this is how it works."


def str2arr(s):
    return np.frombuffer(s.encode('ascii'), dtype=np.uint8)


def fill_repeat(arr, ll):
    if len(arr) >= ll:
        return arr[:ll]
    else:
        mod = ll % len(arr)
        time = int(ll / len(arr))
        return np.concatenate((np.tile(arr, time), arr[:mod]))


def fill_hash(arr, ll):
    if len(arr) >= ll:
        return arr[:ll]
    else:
        hash_arr = np.frombuffer(md5(arr.tobytes()).digest(), dtype=np.uint8)
        return fill_hash(np.concatenate((arr, hash_arr)), ll)


fill = fill_hash


def plot_arr(arr, name):
    length = len(arr)

    plt.figure(figsize=(32, 18))
    plt.subplot(2, 2, 1)
    plt.plot(range(length), arr)
    plt.gca().set_title("plot")

    plt.subplot(2, 2, 2)
    plt.hist(arr, bins=255)
    plt.gca().set_title("hist")

    plt.subplot(2, 2, 3)
    dft_arr = np.fft.fft(arr)
    dft_arr = np.fft.fftshift(dft_arr)
    plt.ylim(0, 3000)
    plt.plot(range(length), dft_arr.real)
    plt.gca().set_title("dft-real")

    plt.subplot(2, 2, 4)
    plt.plot(range(length), dft_arr.imag)
    plt.gca().set_title("dft-image")

    plt.savefig(name + ".svg")
    plt.close()


'''
def mask_xor(key_arr, value_arr):
    key_arr = fill(key_arr, len(value_arr))
    key_arr = np.bitwise_and(key_arr, 0x1f)
    return np.bitwise_xor(key_arr, value_arr)
'''

OFFSET_LOW = 32  # printable char
OFFSET_HIGH = 126  # printable char
VALID_NUM = OFFSET_HIGH - OFFSET_LOW  # 94


def mask_move_encrypt(key_arr, value_arr):
    key_arr = fill(key_arr, len(value_arr))
    key_arr = np.bitwise_and(key_arr, 0x7f)
    res_arr = value_arr - OFFSET_LOW

    res_arr += key_arr
    for i in range(2):
        delta = (res_arr > VALID_NUM).astype(np.uint8) * VALID_NUM
        res_arr -= delta
    return res_arr + OFFSET_LOW


def mask_move_decrypt(key_arr, value_arr):
    key_arr = fill(key_arr, len(value_arr))
    key_arr = np.bitwise_and(key_arr, 0x7f)
    res_arr = value_arr.astype(np.int) - OFFSET_LOW

    res_arr -= key_arr
    for i in range(2):
        delta = (res_arr < 0).astype(np.int) * VALID_NUM
        res_arr += delta
    return (res_arr + OFFSET_LOW).astype(np.uint8)


ARR = str2arr(STR)
if __name__ == '__main__':
    k1 = str2arr('124356')
    arr1 = mask_move_encrypt(k1, ARR)

    k2 = str2arr('hgwueb4W#@R$TYHRTFDGSHYU&Trege4%RTHedgsqwref')
    arr2 = mask_move_encrypt(k2, ARR)

    # plot_arr(ARR, "original")
    # plot_arr(arr1, "simple_pw_hash")
    # plot_arr(arr2, "complex_pw_hash")

    print('\n\nciphertext: ' + '-'*50)
    print(arr1.tobytes().decode('ascii'), '\n')
    print(arr2.tobytes().decode('ascii'), '\n')

    print('\n\ntrue: ' + '-'*50)
    print(mask_move_decrypt(k1, arr1).tobytes().decode('ascii'), '\n')
    print(mask_move_decrypt(k2, arr2).tobytes().decode('ascii'), '\n')

    print('\n\nfake: ' + '-'*50)
    print(mask_move_decrypt(k2, arr1).tobytes().decode('ascii'), '\n')
    print(mask_move_decrypt(k1, arr2).tobytes().decode('ascii'), '\n')
