#!/bin/bash
mkdir build
export rime_dir="./build"
curl -fsSL https://git.io/rime-install | bash -s -- :preset
cp *.yaml build
#cd build
#zip -r nguphing-datapack.zip *
