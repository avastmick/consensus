# Run the docker container (first time)
# docker run -v /home/avastmick/repos/consensus:/consensus:Z --name consensus-box -i -t avastmick/ebook-builder:pandoc
# Start it
# docker start -i consensus-box

# Container commands

# Build a epub book
pandoc -S --toc-depth=1 -o consensus-draft-$(date +"%m-%d-%y").epub pandoc.md chapters/*.md 
# Build a MOBI book
kindlegen *.epub
