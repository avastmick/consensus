# To execute, need to run:
# PowerShell.exe -ExecutionPolicy Unrestricted

cat ..\chapters\*.txt | sc ..\publish\draft.txt

# pandoc -f markdown -t epub --epub-cover-image=bookcover.jpg --epub-stylesheet=epub.css -o ..\publish\draft.epub --smart --toc ..\publish\draft.txt