#!/usr/bin/python3
import time

dicts = [["characters", "nguphing.char"]]

for table in dicts:
    lines = []
    with open("vocabulary/"+table[0]+".csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [x.rstrip("\n").split(",") for x in lines[1:]]
    with open(table[1]+".dict.yaml", "w", encoding="utf-8") as f:
        f.write("""# Rime dictionary
# encoding: utf-8
---
name: {}
version: "{}"
sort: by_weight
...
""".format(table[1], time.strftime("%Y%m%d", time.localtime())))
        for line in lines:
            if line[0] != "#":
                f.write(line[0]+"\t"+line[1]+"\t" +
                        (line[3] if len(line) > 3 else "")+"\n")
    print(table[1]+" converted!")

###

dicts = [["words-legacy", "nguphing.word"],
         ["words", "nguphing.words"],
         ["no-words", "nguphing.nowords"],
         ["map", "nguphing.map"],
         ["phrases", "nguphing.phrases"]]

for table in dicts:
    lines = []
    with open("vocabulary/"+table[0]+".csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [x.rstrip("\n").split(",") for x in lines[1:]]
    with open(table[1]+".dict.yaml", "w", encoding="utf-8") as f:
        f.write("""# Rime dictionary
# encoding: utf-8
---
name: {}
version: "{}"
sort: by_weight
...
""".format(table[1], time.strftime("%Y%m%d", time.localtime())))
        for line in lines:
            if line[0] != "#":
                f.write("\t".join(line[0:2])+"\n")
    print(table[1]+" converted!")
