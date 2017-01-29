# To execute, need to run:
# PowerShell.exe -ExecutionPolicy Unrestricted

cat ..\chapters\*.md | sc ..\publish\draft.md

pandoc -f markdown -t epub --epub-cover-image=bookcover.jpg -o ..\publish\draft.epub --smart --toc ..\publish\draft.md