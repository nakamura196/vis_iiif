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

f = open('ids.csv', 'r')

reader = csv.reader(f)
header = next(reader)

map = {}

for row in reader:

    map[row[0]] = row[1]

f.close()

f = open('output.csv', 'r')

reader = csv.reader(f)
header = next(reader)

arr = []

for row in reader:

    imageURL = row[1]
    
    captureId = row[0]
    captureId = map[captureId] if captureId in map else captureId

    obj = {
        "c_label": "eee",
        "date": "ddd",
        "image": imageURL,
        "label": "aaa",
        "manifest": "bbb",
        "s": captureId,
        "type": "ccc"
    }

    arr.append(obj)
            

f.close()

with open("../data/src/pd_items.json", 'w') as outfile:
    json.dump(arr, outfile, ensure_ascii=False, indent=4,
              sort_keys=True, separators=(',', ': '))
