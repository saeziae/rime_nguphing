#!/usr/bin/python3
import time

def generatedict(filenames,target,width=2):
    chars = []
    for filename in filenames:
        with open("vocabulary/"+filename+".tsv", "r", encoding="utf-8") as f:
            charlist = f.readlines()
            for item in list(charlist)[1:]:
                if item[0] == "#":
                    continue
                chars.append("\t".join(item.rstrip().split("\t")[0:width]))

    with open(target+".dict.yaml", "w", encoding="utf-8") as f:
        f.write("""# Rime dictionary
# encoding: utf-8
---
name: {}
version: "{}"
sort: by_weight
...
""".format(target, time.strftime("%Y%m%d", time.localtime())))
        f.write("\n".join(chars))
    print(target+" converted!")

generatedict(["chars-supp","chars-main"],"nguphing.char",3)
generatedict(["common-word"],"nguphing.common")
generatedict(["words","words-legacy","no-words"],"nguphing.word")
generatedict(["phrases"],"nguphing.phrases")
generatedict(["map"],"nguphing.map")

