#!/bin/bash

## This script pushes specific chapters to the www.avastmick.io website repo

WEBREPO="/home/avastmick/repos/avastmick.io"

CHAPTERS="publish/frontmatter.md  \
        chapters/00-prologue.md  \
        chapters/01-lia-1.0.md  \
        chapters/02-lia-2.0.md  \
        publish/endmatter.md"

cat $CHAPTERS > $WEBREPO/content/book/consensus/chapters.md
