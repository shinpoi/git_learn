# python2 & python3

import argparse

parser = argparse.ArgumentParser(description='just a test of how to use argparse')

parser.add_argument('--aa', '-a', type=int, default=0,
		help='arg of a')
parser.add_argument('--bb', '-b', type=int, default=0,
		help='arg of b')
parser.add_argument('--cc', '-c', type=float, default=0.1,
		help='arg of c')

args = parser.parse_args()

print('a=%d, b=%d, c=%f' % (args.aa, args.bb, args.cc))
print('a + 2b +3.5c = %f' % (args.aa + 2*args.bb + 3.5*args.cc))
