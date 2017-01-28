# To execute, need to run:
# PowerShell.exe -ExecutionPolicy Unrestricted

cat ..\chapters\*.md | sc .\draft.md

pandoc -f markdown -t epub --epub-cover-image=bookcover.jpg -o ..\drafts\draft.epub --smart --toc draft.md