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

arr = []

f = open('data/id.csv', 'r')

reader = csv.reader(f)
header = next(reader)


map = {}
result = {}

for row in reader:
    map[row[0]] = row[1]
    result[row[1]] = {
        "s": row[1]
    }
f.close()

print("# Image")

f = open('data/image.csv', 'r', encoding="utf8", errors='ignore')

reader = csv.reader(f)
header = next(reader)

for row in reader:

    imageURL = row[1]
    captureId = row[0]

    if captureId in result:
        result[captureId]["image"] = imageURL

f.close()

# タイトル

files = {}
files["title"] = "label"
files["database"] = "c_label"
files["publisher"] = "date"
files["right"] = "type"
files["manifest"] = "manifest"

for key in files:

    print("# "+key)

    f = open('data/'+key+'.csv', 'r')

    reader = csv.reader(f)
    header = next(reader)

    arr = []

    for row in reader:

        value = row[1]

        captureId = row[0]

        if captureId in map:

            captureId = map[captureId]

            if captureId in result:
                result[captureId][files[key]] = value


# まとめ

for key in result:
    arr.append(result[key])

with open("../data/src/pd_items.json", 'w') as outfile:
    json.dump(arr, outfile, ensure_ascii=False, indent=4,
              sort_keys=True, separators=(',', ': '))
