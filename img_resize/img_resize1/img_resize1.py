import PIL
from PIL import Image

basewidth = 300
img = Image.open('BetsyandI.jpg')
print(img)
print(img.size[0])
wpercent = (basewidth/float(img.size[0]))
print(wpercent)
print(img.size[1])
hsize = int((float(img.size[1])*float(wpercent)))
print(hsize)
img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
print(img)
#img.save('BetsyandI1.jpg')