"""
Before running script: 
    - Save all data in data.txt
After running script:
    - Check links.txt for links
"""

# Retrive all urls from file also remove github links
import re

foo = open("data.txt")
links = re.findall(
    "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
    foo.read(),
)

# Removing github links
new_list = []
for url in links:
    if "github" not in url:
        new_list.append(url)

# Saving new list to links.txt
thefile = open("links.txt", "w")
for bar in new_list:
    thefile.write("%s\n" % bar)
