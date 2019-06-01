import base64
import json
import os
from PIL import Image
import sys
import urllib.request
import time
import requests
import csv
import glob
import shutil
import os

f = open('ids.csv', 'r')

reader = csv.reader(f)
header = next(reader)

map = {}

for row in reader:

    map[row[0]] = row[1]

f.close()

files = glob.glob('../img/items/*.jpg')
print(len(files))

for file in files:
    filename = file.split("\.")[0]

    if filename in map:
        print(filename)
        new_path = file.replace(filename+".jpg", map[filename+".jpg"])
        shutil.move(file, new_path)
