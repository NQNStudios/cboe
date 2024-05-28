#!/bin/sh -ve

git clone --depth 1 -b 0.9 https://github.com/texus/TGUI.git
cd TGUI
export CLICOLOR_FORCE=1
cmake -D TGUI_CXX_STANDARD=14 .
make
cmake --install .
cd .. # Probably not needed but...
