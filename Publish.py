#!/usr/bin/python

import argparse, datetime, shlex
from subprocess import call
from os import listdir, walk
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
