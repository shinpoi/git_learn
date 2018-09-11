import os
import cv2

jpgfiles = [i for i in os.listdir("./") if i.endswith(".JPG")]

try:
    os.mkdir("./small")
except e:
    pass

# resize to small
for imgFile in jpgfiles:
    if not imgFile.endswith(".JPG"):
        continue
    img = cv2.imread(imgFile)
    if img.shape[0] < img.shape[1]:
        cv2.imwrite("small/" + imgFile, cv2.resize(img, (640, 360)))
    else:
        cv2.imwrite("small/" + imgFile, cv2.resize(img, (360, 640)))

# gen html
html = ""
for imgFile in jpgfiles:
    if not imgFile.endswith(".JPG"):
        continue
    html += '<div class="div_photo"><a href="%s" target="_blank" class="a_photo"><img src="%s" class="img_photo"></img></a></div>\n' % (imgFile, "small/" + imgFile)

with open("index.html", "w") as f:
    f.write(html)
