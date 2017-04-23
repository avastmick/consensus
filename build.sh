#!/bin/bash

# Publishes the book in various formats and sections 

# Currently expects this to be a Hugo web repo
# Make this variable the location where this files will go
# WEBLOCATION="/home/avastmick/repos/avastmick.io/content/book/consensus/chapters"
WEBLOCATION="/home/avastmick/repos/hugo-test/Sites/avastmick.io/content/chapters"

function usage () {
    echo $0: [function] [chapter count]
    echo '        function: word epub web'
    echo '        chapter count: number of chapters to include, or "all" for whole book'
    exit 1
}

function word () {
    local COUNT=0
    CHAPTERS["$1"]=""
    for file in chapters/*.md
    do
      if [[ ! -f "$file" ]]
      then
          continue
      fi  
      if [ "$1" = "all" ]; then
        CHAPTERS["$COUNT"]="$file"
        let COUNT+=1
      elif [ "$COUNT" -eq "$1" ]; then
        break
      else
        CHAPTERS["$COUNT"]="$file"
        let COUNT+=1
      fi                                                             
    done
    echo 'Outputting ' $1 ' chapter(s) of book in MS Word format'
    pandoc -S --toc-depth=1 -o consensus-draft-$(date +"%m-%d-%y").docx ${CHAPTERS[*]}
    echo "...done. Written "${CHAPTERS[*]}" to docx file"
}
#  Need to create individual files and move into the web repo
function web () {
    local COUNT=0
    CHAPTERS["$1"]=""
    for file in chapters/*.md
    do
      if [[ ! -f "$file" ]]
      then
          continue
      fi 
      if [ "$1" = "all" ]; then
        CHAPTERS["$COUNT"]="$file"
        let COUNT+=1
      elif [ "$COUNT" -eq "$1" ]; then
        break
      else
        CHAPTERS["$COUNT"]="$file publish/web-interstitial.md"
        let COUNT+=1
      fi                                                             
    done

    echo 'Publishing ' $1 ' chapter(s) of book to website'

    # Move this into a function to create the chapter files and copy over
    cat publish/web-frontmatter.md ${CHAPTERS[*]} publish/web-endmatter.md > $WEBLOCATION/chapters.md

    echo "...done. Written "${CHAPTERS[*]}" to web site"
}

function epub () {
    local COUNT=0
    CHAPTERS["$1"]=""
    for file in chapters/*.md
    do
      if [[ ! -f "$file" ]]
      then
          continue
      fi 
      if [ "$1" = "all" ]; then
        CHAPTERS["$COUNT"]="$file"
        let COUNT+=1
      elif [ "$COUNT" -eq "$1" ]; then
        break
      else
        CHAPTERS["$COUNT"]="$file"
        let COUNT+=1
      fi                                                            
    done
    echo 'Outputting ' $1 ' chapter(s) of book in epub'
    pandoc -S --toc-depth=1 -o consensus-draft-$(date +"%m-%d-%y").epub publish/epub-frontmatter.md ${CHAPTERS[*]}

    echo "...done. Written "${CHAPTERS[*]}" to epub file"
}

if [ $# -ne 2 ]; then
    usage
elif [ $1 == 'web' ]; then
    web $2
elif [ $1 == 'epub' ]; then
    epub $2
elif [ $1 == 'word' ]; then
    word $2
elif [[ condition ]]; then
    usage
fi
