#!/usr/bin/python3
import time

dicts = ["nguphing.char", "nguphing.word", "nguphing.map"]

for table in dicts:
    lines = []
    with open("source/"+table+".csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [x.rstrip("\n").split(",") for x in lines[1:]]
    with open(table+".dict.yaml", "w", encoding="utf-8") as f:
        f.write("""# Rime dictionary
# encoding: utf-8
---
name: {}
version: "{}"
sort: by_weight
...
""".format(table, time.strftime("%Y%m%d", time.localtime())))
        for line in lines:
            if line[0] != "#":
                f.write("\t".join(line[0:2])+"\n")
    print(table+" converted!")
