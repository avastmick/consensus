#!/usr/bin/python

import argparse

def epub(_chapters):
    print("Output to epub format, number of chapters: "+_chapters)

def web(_chapters):
    print("Publish to web location, number of chapters: "+_chapters)

def word(_chapters):
    print("Output to MS Word format, number of chapters: "+_chapters)

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
