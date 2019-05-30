# -*- coding: utf-8 -*-

# Description: retrieves the date (year or century) of items
# Example usage:
#   python get_dates.py ../data/src/pd_items.json ../data/dates.json ../data/item_dates.json year
#   python get_dates.py ../data/src/pd_items.json ../data/centuries.json ../data/item_centuries.json century

from collections import Counter
import json
import math
from pprint import pprint
import re
import sys
from SPARQLWrapper import SPARQLWrapper
import urllib.request

OUTPUT_FILE = "../data/src/pd_items.json"

loop_flg = True
page = 1

api_url = "http://iiif2.dl.itc.u-tokyo.ac.jp/api"

arr = []

while loop_flg:
    url = api_url + "/items?page=" + str(page)
    print(url)

    page += 1

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    response_body = response.read().decode("utf-8")
    data = json.loads(response_body.split('\n')[0])

    if len(data) > 0:
        for i in range(len(data)):
            item = data[i]

            obj = {}
            obj["s"] = item["dcterms:identifier"][0]["@value"]
            obj["label"] = item["dcterms:title"][0]["@value"]
            obj["c_label"] = item["dcndl:digitizedPublisher"][0]["@value"] if "dcndl:digitizedPublisher" in item else  ""
            obj["type"] = item["dcterms:rights"][0]["@id"] if "dcterms:rights" in item else ""
            obj["manifest"] = item["dcterms:references"][0]["@id"]
            obj["date"] = item["uterms:databaseLabel"][0]["@value"] if "uterms:databaseLabel" in item else ""
            imageURL = ""

            if len(item["o:media"]) > 0:
                mid = item["o:media"][0]["@id"]

                request = urllib.request.Request(mid)
                response = urllib.request.urlopen(request)

                response_body = response.read().decode("utf-8")
                media = json.loads(response_body.split('\n')[0])

                imageURL = media["o:thumbnail_urls"]["medium"]

            else:
                imageURL = item["dcterms:source"][0]["@id"] if "dcterms:source" in item else ""

            obj["image"] = imageURL

            arr.append(obj)
        if page > 100:
            loop_flg = False
    else:
        loop_flg = False

with open(OUTPUT_FILE, 'w') as outfile:
    json.dump(arr, outfile, ensure_ascii=False, indent=4,
              sort_keys=True, separators=(',', ': '))
