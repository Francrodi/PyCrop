from PIL import Image
import os

srcPath = './src'

for file in os.listdir(srcPath):
    print('Cropeando: ', file)
    img = Image.open(srcPath + '/' + file)
    crop = (16*img.height - 9*img.width) / 32
    box = (0, crop, img.width, img.height - crop)
    imgCropped = img.crop(box)
    imgCropped.save(srcPath + '/' + file, 'jpeg')
    print(file, 'Done')
