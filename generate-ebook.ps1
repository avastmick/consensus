# To execute, need to run: 
# PowerShell.exe -ExecutionPolicy Unrestricted 
 
cat .\chapters\*.md | sc .\draft.md 
 
# Using gitbok cli
# gitbook mobi ./ ./draft.mobi

# pandoc -f markdown -t epub --epub-cover-image=bookcover.jpg -o ..\drafts\draft.epub --smart --toc draft.md