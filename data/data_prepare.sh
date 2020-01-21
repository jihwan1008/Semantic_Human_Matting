#!/bin/sh

ROOT=./aisegment/matting

find "$ROOT" -type f -name '*.png or *.jpg' -o -exec echo convert {} -background white -alpha remove -alpha off {} \;
python data_prepare.py
