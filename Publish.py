#!/usr/bin/python

import argparse, datetime, shlex
from subprocess import call
from os import listdir, walk, mkdir, rmdir, rename
from os.path import isfile, join


def epub(_chapters):
    print("Output to epub format, number of chapters: "+_chapters)
    # TODO try to make OS independent and read from properties file
    fileList = ['publish/epub-frontmatter.md']

    for dirname, dirnames, filenames in walk('chapters'):
        for filename in filenames:
            fileList += [(join(dirname, filename))]

    fileListStr = ""
    if _chapters == 'all':
        fileListStr += ' '.join(fileList)
    else: # note: add '1' to slice to take into account frontmatter
        fileListStr += ' '.join(fileList[0:int(_chapters)+1])

    print "Publishing as epub the following: "+fileListStr

    date = datetime.date.today()
    fileName = 'consensus-draft-'+str(date)+'.epub '

    pandocCmd = 'pandoc -S --toc-depth=1 -o '+fileName+fileListStr
    args = shlex.split(pandocCmd)

    call(args)

    print("Published book as: "+fileName)

def web(_chapters):
    print("Publish to web location, number of chapters: "+_chapters)
    titleRegexp = "FILENAME"
    # 00:01:01
    timestamp = "TIMESTAMP"
    # 
    timeNow = str(datetime.datetime.now())
    print(timeNow)
    draftDir = "web-draft"

    webLocation = "/home/avastmick/repos/hugo-test/Sites/avastmick.io/content/chapters"
    # Create a tmp dir (web-draft)
    mkdir(draftDir)
    # Create frontmatter tmp with the right title and timestamp

    # suck in frontmatter

    # overwrite values in str

    fileList = []

    for dirname, dirnames, filenames in walk('chapters'):
        for filename in filenames:
            fileList += [(join(dirname, filename))] 
    fileListStr = ""
    if _chapters == 'all':
        fileListStr += ' '.join(fileList)
    else: 
        fileListStr += ' '.join(fileList[0:int(_chapters)])

    print "Publishing as epub the following: "+fileListStr 
    # Create a file for each chapter [prologue.md, chapter-1.md, chapter-2.md]

    # Concat the frontmatter str and file contents

    # write file to tmp dir

    # mv the files to the web location
    # mv web-draft/*.md ../avastmick/...
    # delete the tmp dir with all the files
    rmdir(draftDir) 

def word(_chapters):
    print("Output to MS Word format, number of chapters: "+_chapters)
    fileList = []

    for dirname, dirnames, filenames in walk('chapters'):
        for filename in filenames:
            fileList += [(join(dirname, filename))]

    fileListStr = ""
    if _chapters == 'all':
        fileListStr += ' '.join(fileList)
    else: # note: add '1' to slice to take into account frontmatter
        fileListStr += ' '.join(fileList[0:int(_chapters)+1])

    print "Publishing as epub the following: "+fileListStr

    date = datetime.date.today()
    fileName = 'consensus-draft-'+str(date)+'.docx '

    pandocCmd = 'pandoc -S --toc-depth=1 -o '+fileName+fileListStr
    args = shlex.split(pandocCmd)

    call(args)

    print("Published book as: "+fileName)

# Handle input and pass to publish functions
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Publishes book content to multiple formats")
    parser.add_argument('format', help="The format to output (default: %(default)s)", nargs='?', choices=["epub", "word", "web"], default="epub")
    parser.add_argument('chapters', help="Number of chapters (e.g. 5, or \"all\") (default: %(default)s)", nargs='?', default="all")

    args = parser.parse_args()

    if args.format == "epub":
        epub(args.chapters)
    elif args.format == "word":
        word(args.chapters)
    elif args.format == "web":
        web(args.chapters)
