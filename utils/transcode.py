# -*- coding: utf-8 -*-
# python3

"""
Convert encoding of filename and content. Use for windows.

Usage:
python3 transcode.py  -->  convert SHIST-JIS to GBK from current path
"""

import os
import logging
from os.path import isfile, isdir, join
from optparse import OptionParser

# parser
parser = OptionParser()
parser.add_option("-p", "--path",
                  dest="p", default='.',
                  help="path | default: .")

parser.add_option("-e", "--extend",
                  dest="e", default='txt',
                  help="extends list, split by ',' | default: txt")

# gb18030: gb2312 + gbk -> gb18030. cn windows
parser.add_option("-i", "--input",
                  dest="i", default='gb18030',
                  help="input encoding | default: gb18030")

# cp932: update version of shift-jis. jp windows
parser.add_option("-o", "--output",
                  dest="o", default='cp932',
                  help="output encoding | default: cp932")

#############################################


class Converter:
    in_code = ''
    out_code = ''

    def __init__(self, in_code, out_code, extensions):
        self.in_code = in_code
        self.out_code = out_code
        self.extensions = extensions

    def convert(self, path):
        path = os.path.abspath(path)
        if not isdir(path):
            raise ValueError('Path: {} is not a directory!'.format(path))
        for re_path in os.listdir(path):
            target = join(path, re_path)
            if any([target.endswith(ext) for ext in self.extensions]):
                self.convert_content(target)
            if isfile(target):
                self.convert_filename(target)
            if isdir(target):
                self.convert(target)
        self.convert_filename(path)

    def convert_filename(self, path: str):
        dirname = os.path.dirname(path)
        basename = os.path.basename(path)
        try:
            new_name = basename.encode(self.in_code).decode(self.out_code)
            os.rename(path, join(dirname, new_name))
            logging.debug('{} -> {}'.format(basename, new_name))
        except UnicodeDecodeError:
            logging.error('Can not convert file: {}'.format(path))

    def convert_content(self, path: str):
        try:
            with open(path, 'rb') as f:
                text_b = f.read().decode(self.out_code)
            with open(path, 'wb') as f:
                f.write(text_b.encode('utf-8'))
        except UnicodeDecodeError:
            logging.error('Can not convert content in: {}'.format(path))


if __name__ == '__main__':
    options, args = parser.parse_args()
    converter = Converter(
        in_code=options.i,
        out_code=options.o,
        extensions=options.e
    )
    converter.convert(options.p)
