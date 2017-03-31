# Run the docker container (first time)
# docker run -v C:\Users\avastmick\repos\consensus:/consensus --name consensus-box -i -t avastmick/ebook-builder:pandoc
# Start it
# docker start -i consensus-box

# Container commands

# Build a epub book
# pandoc -S --toc-depth=1 -o consensus-draft-$(date +"%m-%d-%y").epub chapters/*.md 
# pandoc -S -o consensus-draft.epub draft.md
# Build a MOBI book
# kindlegen *.epub



# Brain tree photo
# photo credit: Eduardo Mueses <a href="http://www.flickr.com/photos/38692570@N00/8650127689">Make the Connections</a> via <a href="http://photopin.com">photopin</a> <a href="https://creativecommons.org/licenses/by-nc-nd/2.0/">(license)</a>


# Cogs photo credit
# photo credit: Piyushgiri Revagar <a href="http://www.flickr.com/photos/123868529@N03/28777007826">Clever Cogs!</a> via <a href="http://photopin.com">photopin</a> <a href="https://creativecommons.org/licenses/by-nc-nd/2.0/">(license)</a>