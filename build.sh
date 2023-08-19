#!/usr/bin/env bash

if [ $# != 1 ]; then
    echo "usage: build.sh <target>"
    echo "Script that build a selected Manim scene and copies the source and target to a desired location (in file target.txt)."
    exit
fi

if [ ! -f "target.txt" ]; then
    echo "Create target.txt to say where the result should be copied to"
    exit
fi

target="$1"
name="$(basename -s '.py' "$target")"
page_target="$(cat "./target.txt")/build/"
manim -qh "$target" Main \
    && cp "$target" "$page_target/$name.py" \
    && convert "./media/images/$name/Main"* -resize 160x "$page_target/$name.png"
