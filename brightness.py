from PIL import Image, ImageEnhance
import os

arr = os.listdir('.')
arr.remove('brightness.py')

for i in range(len(arr)):
    im = Image.open(arr[i])
    enhancer = ImageEnhance.Brightness(im)
    factor = 1 #change factor, 1 will output normal
    im_output = enhancer.enhance(factor)
    im_output.save(arr[i])
    im.close() 