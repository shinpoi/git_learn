import os

jpgfiles = [i for i in os.listdir("./") if i.endswith(".JPG")]
arwfiles = [i[:-3] + "ARW" for i in jpgfiles]

arwlist = os.listdir("./arw/")
for img in arwlist:
    if not img in arwfiles:
        os.remove("./arw/" + img)
