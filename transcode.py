# encode: utf-8
# python3
# windows only

import os
import sys
from optparse import OptionParser

# parser
parser = OptionParser()
parser.add_option("-f", "--filename",
                  action="store_true", dest="f", default=True,
                  help="transcode filename? | default: true")
                  
parser.add_option("-F", "--foldername",
                  action="store_true", dest="F", default=True,
                  help="transcode foldername? | default: true")

parser.add_option("-c", "--content",
                  action="store_true", dest="c", default=False,
                  help="transcode file content? | default: false")

parser.add_option("-e", "--extend",
                  dest="e", default='txt',
                  help="extends list, split by ',' | default: txt")
     
parser.add_option("-p", "--path",
                  dest="p", default='.',
                  help="path | default: .")

parser.add_option("-i", "--input",
                  dest="i", default='gbk',
                  help="input code | default: gbk")
### cp932: a update veersion of shift-jis ###

parser.add_option("-o", "--output",
                  dest="o", default='cp932',
                  help="output code | default: cp932")

options, args = parser.parse_args()
path = options.p
in_code = options.i
out_code = options.o
extends = options.e
while True:
    if extends.startswith('"'):
        extends = extends[1:]
    elif extends.endswith('"'):
        extends = extends[:-1]
    else:
        break

#############################################
# folder
if options.F:
    print("\n----------\ntrans folders:\n----------\n")
    for i in os.walk(path):
        root, folders, files = i
        print("walk in: %s" % root)
        for folder in folders:
            full_path =  "%s\%s" % (root, folder)
            new_folder = folder.encode(in_code).decode(out_code)
            os.rename(full_path, "%s\%s" % (root, new_folder))
            try:
                print("  - %s ------> %s" % (folder, new_folder))
            except:
                pass

# file
if options.f:
    print("\n----------\ntrans files:\n----------\n")
    for i in os.walk(path):
        root, folders, files = i
        print("walk in: %s" % root)
        for file in files:
            full_path =  "%s\%s" % (root, file)
            new_file = file.encode(in_code).decode(out_code)
            os.rename(full_path, "%s\%s" % (root, new_file))
            try:
                print("  - %s ------> %s" % (file, new_file))
            except:
                pass
            
# content
if options.c:
    print("\n----------\ntrans content:\n----------\n")
    for i in os.walk(path):
        root, folders, files = i
        print("walk in: %s" % root)
        for file in files:
            full_path =  "%s\%s" % (root, file)
            with open(full_path, 'rb') as f:
                origin_c = f.read
            trans_c = origin_c.decode(in_code).encode(out_code)
            with open(full_path, 'w') as f:
                f.write(trans_c)
            print("  - trans contets: file")
