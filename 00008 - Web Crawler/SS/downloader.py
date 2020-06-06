import sys, re, requests
from PIL import Image
from io import BytesIO

# check for cli arguments
print(sys.argv)
if len(sys.argv) > 2:
    sourcefile = sys.argv[1]
    suffix = sys.argv[2]
elif len(sys.argv) > 1:
    sourcefile = sys.argv[1]
    suffix = ""
    print("No suffix provided, so no suffix will be in the filename")
else:
    print("Error! Need a path to a file containing the html to search and a suffix for the file name...")
    quit()
print(sourcefile)

# open file, read contents and close file
textfile = open(sourcefile, 'r')
print(textfile)
filetext = textfile.read()
print(filetext)
textfile.close()

# search file and perform regex to find all matches
matches = re.findall(
    "(?:\s*<div.*>\n){2}\s*<img src=\"(\/.*.png)\".alt=\".*\">\n\s*<h2>(.*)<\/h2>\n(?:\s*<div.*>\n){2}(?:.*<\/div>.*\n){4}",
    filetext)
print(matches)
for match in matches:
    # retrieve file from url and save to disk
    name = f"{match[1]}{suffix}.png"
    filename = f"./downloads/{name}"
    url = f"https://rocket-league.com{match[0]}"
    print(f"Trying to retrieve '{name}' from '{url}'")

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.save(filename)
    img = ""

    print(f"Saved '{name}'")