# encode: utf-8

b = b'abcdefg'
print(b)
# > b'abcdefg'

# > 0x61 0x62 0x63 0x64 0x65 0x66 0x67
for i in b:
    print(hex(i), end=' ')

# > 0b1100001 0b1100010 0b1100011 0b1100100 0b1100101 0b1100110 0b1100111
for i in b:
    print(bin(i), end=' ')

type(i)
# > int
