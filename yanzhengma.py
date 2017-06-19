#-*- coding:utf8 -*-
from PIL import Image
import os
import subprocess



im = Image.open("11.jpg")
# 转化到灰度图
imgry = im.convert('L')
imgry.show()
pixels = imgry.load()
#二值化
for x in range(imgry.width):
  for y in range(imgry.height):
      pixels[x, y] = 255 if pixels[x, y] > 20 else 0



def image_to_string(img, cleanup=True, plus=''):
    # cleanup为True则识别完成后删除生成的文本文件
    # plus参数为给tesseract的附加高级参数
    subprocess.check_output('tesseract ' + img + ' ' +
                            img + ' ' + plus, shell=True)  # 生成同名txt文件
    text = ''
    with open(img + '.txt', 'r') as f:
        text = f.read().strip()
    if cleanup:
        os.remove(img + '.txt')
    return text

print(image_to_string('21.jpg'))