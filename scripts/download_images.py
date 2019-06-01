# -*- coding: utf-8 -*-

# Description: downloads the smallest cropped image captures from a list of items
# Example usage:
#   python download_images.py ../data/src/pd_items.json ../img/items/ b
# Derivative types:
#   t: 150
#   b: 100 (cropped)
#   f: 192
#   r: 300
#   w: 760
#   q: 1600
#   v: 2560
#   g: Original

import base64
import json
import os
from PIL import Image
import sys
import urllib.request
import time
import requests
import csv


def isValidImage(fileName):
    isValid = True
    try:
        im = Image.open(fileName)
        # do stuff
    except IOError:
        # filename not an image file
        isValid = False
    except:
        isValid = False
    return isValid


# config
overwriteExisting = False

f = open('output.csv', 'r')

reader = csv.reader(f)
header = next(reader)

i = 0

for row in reader:

    if i % 20 == 0:
        print(i)

    i += 1

    imageURL = row[1]
    
    captureId = row[0]
    fileName = "../img/items/" + captureId + ".jpg"

    # save file if not found or overwrite is set to True
    if overwriteExisting or not os.path.isfile(fileName):

        if "iiif2" not in imageURL:
            time.sleep(0.1)  # sleep(秒指定)

        # Base64を扱うための標準ライブラリ

        # 送信先のURL
        url = imageURL

        try:
            # time.sleep(0.01)  # sleep(秒指定)
            r = requests.get(url)

            if r.status_code == 200:
                with open(fileName, 'wb') as f:
                    f.write(r.content)

        except:
            print(url)
            

f.close()

