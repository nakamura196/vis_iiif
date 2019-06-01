import csv


dt = []
dt.append(["id", "url"])

# --------

f = open('tmp/media.csv', 'r')

reader = csv.reader(f)
header = next(reader)
for row in reader:
    id = row[1]
    url = "http://iiif2.dl.itc.u-tokyo.ac.jp/files/square/"+row[7]+"."+row[8]
    dt.append([id, url])

f.close()

# --------

f = open('tmp/thumb.csv', 'r')

reader = csv.reader(f)
header = next(reader)

map = {}

for row in reader:
    id = row[1]
    pid = row[2]
    v = ""
    if pid == "10":

        v = row[6]
    else:
        v = row[7]

    if id not in map:
        map[id] = {}

    obj = map[id]
    obj[pid] = v

f.close()

for id in map:

    obj = map[id]

    if "15" in obj and obj["15"] != "http://dl.ndl.go.jp/ja/iiif_license.html":
        if "11" in obj and "10" in obj:
            dt.append([obj["10"], obj["11"]])

# --------

# ファイルオープン
f = open('output.csv', 'w')
writer = csv.writer(f, lineterminator='\n')

# 出力
writer.writerows(dt)

# ファイルクローズ
f.close()
