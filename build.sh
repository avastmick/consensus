#!/bin/bash

# Publishes the book in various formats and sections 
WEBREPO="/home/avastmick/repos/avastmick.io"

function usage () {
    echo $0: [function] [chapter count]
    echo functions: word epub web
    echo 'chapter count: number of chapters to include, or "all" for whole book'
    exit 1
}

function word () {
    echo 'Outputting '+$1+' chapter(s) of book in MS Word format'
}

function publishToWeb () {
    echo 'Publishing '+$1+' chapter(s) of book to website'

    local CHAPTERS="one"

    # cat $CHAPTERS > $WEBREPO/content/book/consensus/chapters.md
}

function epub () {
    echo 'Outputting '+$1+' chapter(s) of book in epub'
    pandoc -S --toc-depth=1 -o consensus-draft-$(date +"%m-%d-%y").epub frontmatter.md chapters/*.md
}

if [ $# -ne 2 ]; then
    usage
elif [ $1 == 'web' ]; then
    echo web called for $2 chapters
elif [ $1 == 'epub' ]; then
    epub $2
elif [ $1 == 'word' ]; then
        #statements
fi
