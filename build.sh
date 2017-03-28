# Run the docker container (first time)
# docker run -v C:\Users\avastmick\repos\consensus:/consensus --name consensus-box -i -t avastmick/ebook-builder:pandoc
# Start it
# docker start -i consensus-box

# Container commands

# Build a epub book
# pandoc -S -o consensus-draft-$(date +"%m-%d-%y").epub chapters/*.md 
# Build a MOBI book
# kindlegen *.epub
