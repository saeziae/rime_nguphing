#!/bin/bash
cp rime-prelude/key_bindings.yaml .
cp rime-essay/essay.txt rime-prelude/symbols.yaml rime-prelude/punctuation.yaml rime-prelude/default.yaml .
rime_deployer --compile nguphing.schema.yaml
rime_deployer --compile nguphing-shanghai.schema.yaml
rm key_bindings.yaml punctuation.yaml symbols.yaml default.yaml essay.txt
zip nguphing-$(date '+%Y%m%d').zip build/*.bin build/*.yaml
