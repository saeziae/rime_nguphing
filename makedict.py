#!/usr/bin/python3
import time
lines = []
with open("nguphing.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()
lines = [x.split(",") for x in lines[1:]]
with open("nguphing.dict.yaml", "w", encoding="utf-8") as f:
    f.write("""# Rime dictionary
# encoding: utf-8
---
name: nguphing
version: "{}"
sort: by_weight
use_preset_vocabulary: true
import_tables:
  - nguphing.word
...
""".format(time.strftime("%Y%m%d", time.localtime())))
    for line in lines:
        f.write("\t".join(line[0:3])+"\n")
print("OK")

lines = []
with open("nguphing.word.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()
lines = [x.split(",") for x in lines[1:]]
with open("nguphing.word.dict.yaml", "w", encoding="utf-8") as f:
    f.write("""# Rime dictionary
# encoding: utf-8
---
name: nguphing.word
version: "{}"
sort: by_weight
...
""".format(time.strftime("%Y%m%d", time.localtime())))
    for line in lines:
        f.write("\t".join(line[0:2])+"\n")
print("OK")
