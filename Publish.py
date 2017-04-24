#!/usr/bin/python

import argparse, datetime, shlex, yaml
from string import Template
from subprocess import call
from os import path, listdir, walk, mkdir, rmdir, rename
from os.path import isfile, join

CONFIG_FILE = 'publish-config.yml'
cfg = ''

def loadConfig():
    global cfg
    with open(CONFIG_FILE, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

def mobi(_chapters):
    print("Output to mobi (Kindle) format, number of chapters: "+_chapters)
    if not path.exists(cfg['draftDir']):
        mkdir(cfg['draftDir'])
    # Find the epub and convert
    epubfound = False
    for dirname, dirnames, filenames in walk(cfg['draftDir']):
        for filename in filenames:
            if filename.endswith('.epub'):
                epubfound = True
                print("Got epub file to convert: "+filename)
                break
    if not epubfound:
        epub(_chapters)

    kindlegenCmd = 'kindlegen '+join('.',cfg['draftDir'],"*.epub")
    args = shlex.split(kindlegenCmd)
    print("Converting .epub...")
    try:
        call(args)
    except:
        print("Kindlegen not found or not functioning. Is it installed?")
        exit(-1)
    print("...done.")
    print("Published book as .mobi")    

def epub(_chapters):
    print("Output to epub format, number of chapters: "+_chapters)
    if not path.exists(cfg['draftDir']):
        mkdir(cfg['draftDir'])

    fileList = [join(cfg['publishDir'],cfg['epub-frontmatter'])]

    for dirname, dirnames, filenames in walk(cfg['sourceDir']):
        for filename in filenames:
            fileList += [(join(dirname, filename))]

    fileListStr = ""
    if _chapters == 'all':
        fileListStr += ' '.join(fileList)
    else: # note: add '1' to slice to take into account frontmatter
        fileListStr += ' '.join(fileList[0:int(_chapters)+1])

    print "Publishing as epub the following: "+fileListStr

    date = datetime.date.today()
    fileName = join(cfg['draftDir'],cfg['book-name']+'-draft-'+str(date)+'.epub ')

    pandocCmd = 'pandoc -S --toc-depth=1 -o '+fileName+fileListStr
    args = shlex.split(pandocCmd)
    try:
        call(args)
    except:
        print("Pandoc not found or not functioning. Is it installed?")
        exit(-1)

    print("Published book as: "+fileName)

def web(_chapters):

    print("Publish to web location, number of chapters: "+_chapters)
    # Create a tmp dir
    if not path.exists(cfg['draftDir']):
        mkdir(cfg['draftDir'])
    # suck in frontmatter into template
    frontmatter = []
    with open(join(cfg['publishDir'],cfg['web-frontmatter']), 'r') as fmfile:
        frontmatter=fmfile.read()

    # Create the file list
    fileList = []
    for dirname, dirnames, filenames in walk(cfg['sourceDir']):
        for filename in filenames:
            fileList += [(join(dirname, filename))] 
    # Trim according to num chapters
    if _chapters != 'all':
        fileList = fileList[0:int(_chapters)]

    print "Publishing as epub the following: "+str(fileList) 
    # Loop over files to be created
    filecount = 0
    for filename in fileList:
        chapter = ""
        # overwrite values in frontmatter str 
        fm = Template(str(frontmatter))
        if filecount == 0:
            chapter = fm.substitute(FILENAME=cfg['firstFile'], TIMESTAMP='00:0'+str(filecount+1)+':0'+str(filecount+1))
        else:
            chapter = fm.substitute(FILENAME=cfg['fileNameBase']+'-'+str(filecount), TIMESTAMP='00:0'+str(filecount+1)+':0'+str(filecount+1))
        # concat
        with open(filename, 'r') as chaptfile:
            chapter += chaptfile.read()  
            chaptfile.close()
        # write out chapter file
        chaptname = ""
        if filecount == 0:
            chaptname = cfg['firstFile']+cfg['ext']
        else:
            chaptname = cfg['fileNameBase']+'-'+str(filecount)+cfg['ext']
        chaptfile = open(join(cfg['draftDir'],chaptname), "w")
        chaptfile.write(chapter)
        chaptfile.close()

        # increment counter
        filecount += 1
    # Add end matter chapter
    chapter = fm.substitute(FILENAME=cfg['fileNameBase']+'-'+str(filecount), TIMESTAMP='00:0'+str(filecount+1)+':0'+str(filecount+1))
    with open(join(cfg['publishDir'],cfg['web-endmatter']), 'r') as chaptfile:
        chapter += chaptfile.read() 
        chaptfile.close()
    # write out chapter file
    chaptfileStr = join(cfg['draftDir'],cfg['fileNameBase']+'-'+str(filecount)+cfg['ext'])
    chaptfile = open(chaptfileStr, "w")
    chaptfile.write(chapter)
    chaptfile.close()
    # mv the files to the web location
    for dirname, dirnames, filenames in walk(cfg['draftDir']):
        for filename in filenames:
            if cfg['ext'] in filename.lower():
                rename(join(dirname, filename),join(cfg['webLocation'],filename))
            elif ".epub" in filename.lower():
                rename(join(dirname, filename),join(cfg['webLocation'],cfg['book-name']+'-'+"chapters-1-"+str(filecount)+".epub")) 
            elif ".mobi" in filename.lower():
                rename(join(dirname, filename),join(cfg['webLocation'],cfg['book-name']+'-'+"chapters-1-"+str(filecount)+".mobi"))

def word(_chapters):
    print("Output to MS Word format, number of chapters: "+_chapters)
    if not path.exists(cfg['draftDir']):
        mkdir(cfg['draftDir'])

    fileList = []
    for dirname, dirnames, filenames in walk(cfg['sourceDir']):
        for filename in filenames:
            fileList += [(join(dirname, filename))]

    fileListStr = ""
    if _chapters == 'all':
        fileListStr += ' '.join(fileList)
    else: # note: add '1' to slice to take into account frontmatter
        fileListStr += ' '.join(fileList[0:int(_chapters)+1])

    print "Publishing as epub the following: "+fileListStr

    date = datetime.date.today()
    fileName = join(cfg['draftDir'],cfg['book-name']+'-draft-'+str(date)+'.docx ')

    pandocCmd = 'pandoc -S --toc-depth=1 -o '+fileName+fileListStr
    args = shlex.split(pandocCmd)

    try:
        call(args)
    except:
        print("Pandoc not found or not functioning. Is it installed?")
        exit(-1)

    print("Published book as: "+fileName)

# Handle input and pass to publish functions
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Publishes book content to multiple formats")
    parser.add_argument('format', help="The format to output (default: %(default)s)", nargs='?', choices=["epub", "mobi", "word", "web"], default="epub")
    parser.add_argument('chapters', help="Number of chapters (e.g. 5, or \"all\") (default: %(default)s)", nargs='?', default="all")

    args = parser.parse_args()

    if args.format == "epub":
        loadConfig()
        epub(args.chapters)
    elif args.format == "mobi":
        loadConfig()
        mobi(args.chapters)
    elif args.format == "word":
        loadConfig()
        word(args.chapters)
    elif args.format == "web":
        loadConfig()        
        web(args.chapters)
