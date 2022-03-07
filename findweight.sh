#!/bin/sh
if [ -n "$1" ]; then 
cat rime-essay/essay.txt | egrep "^$1\b" | sed "s/[^0-9]//g"
fi