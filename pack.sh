#!/bin/bash
cp rime-prelude/key_bindings.yaml .
cp rime-essay/essay.txt rime-prelude/symbols.yaml rime-prelude/punctuation.yaml rime-prelude/default.yaml .
find . -maxdepth 1 -name "*.schema.yaml" -exec rime_deployer --compile {} \;
rm key_bindings.yaml punctuation.yaml symbols.yaml default.yaml essay.txt
zip nguphing-$(date '+%Y%m%d')-bin.zip build/*.bin build/*.yaml
zip nguphing-$(date '+%Y%m%d')-yaml.zip *.yaml