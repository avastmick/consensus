# To execute, need to run: 
# PowerShell.exe -ExecutionPolicy Unrestricted 
 
cat .\chapters\*.md | sc .\draft.md 

pandoc -S --toc-depth=1 -o consensus-draft.epub pandoc.md draft.md
kindlegen *.epub

rm draft.md
