# encode: ascii
# a simple xor encrypt. just support ascii

import numpy as np

ENCODE = 'ascii'
TRUNCATE = np.uint8(0x1f)  # set high 3 bit to 0


# pad bs to multiples of block_len by x00
# bs: bytes, block_len: int
def pad(bs, block_len=8):
    mod = len(bs) % block_len
    if mod == 0:
        return bs
    else:
        return bs + b'\x00' * (block_len - mod)


# key: str, value: str.
def mask(key, value):
    b_key = pad(key.encode(ENCODE))
    b_value = pad(value.encode(ENCODE), len(b_key))

    k_arr = np.frombuffer(b_key, dtype=np.uint8)
    v_arr = np.frombuffer(b_value, dtype=np.uint8)
    k_arr = np.bitwise_and(k_arr, TRUNCATE)

    len_k = k_arr.shape[0]
    len_v = v_arr.shape[0]

    if len_v >= len_k:
        k_arr = np.tile(k_arr, int(len_v / len_k))
    else:
        k_arr = k_arr[:len_v]

    return np.bitwise_xor(v_arr, k_arr).tobytes().decode(ENCODE)


# example
if __name__ == '__main__':
    k = 'any passwd'
    fake_k = 'some bad password'

    value1 = "secret"
    en_v1 = mask(k, value1)
    print("encry v1 = " + en_v1)
    de_v1 = mask(k, en_v1)
    print("decry v1 = " + de_v1)
    fake_v1 = mask(fake_k, en_v1)
    print("fake  v1 = " + fake_v1)

    print("")

    value2 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt"
    en_v2 = mask(k, value2)
    print("encry v2 = " + en_v2)
    de_v2 = mask(k, en_v2)
    print("decry v2 = " + de_v2)
    fake_v2 = mask(fake_k, en_v2)
    print("fake  v2 = " + fake_v2)

'''
# output:

encry v1 = rkjreu
decry v1 = secret
fake  v1 = qdgwew

encry v2 = Ma{em!jstqm dolos.zit!bnbp, consdm}ettq#f`ipisich`n emjw+$sed do!k`usllg'pempor h`jidhgvip
decry v2 = Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt
fake  v2 = Nnv`m#kwtql#ghcmw.zit!bna!%cmowdm|fws~!b`ipisickoc%eoks+$rfg'km%k`usllg$hhpms$h`kjgohtmp
'''
