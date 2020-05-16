import bs4 as bs
import urllib.request
import urllib
import csv

source = urllib.request.urlopen('https://yugioh.fandom.com/wiki/Set_Card_Lists:Deck_Build_Pack:_Mystic_Fighters_(OCG-JP)').read()

soup = bs.BeautifulSoup(source,'lxml')
print(soup.encode("utf-8"))

f = csv.writer(open("OUTPUT.csv", "w", encoding="utf-8"))

links = soup.find_all('a')

for link in links:
    print(link)
    f.writerow([str(link)])

import urllib
from urllib.request import Request, urlopen
import csv
import requests
from PIL import Image
from io import BytesIO

url = 'https://vignette.wikia.nocookie.net/yugioh/images/a/a6/TenThousandDragon-IGAS-JP-10000ScR.png/revision/latest/scale-to-width-down/118?cb=20191025013811'

urllib.request.urlretrieve(url, "pic1.png")

response = requests.get(url)
name = f"test.png"
filename = f"./downloads/{name}"
img = Image.open(BytesIO(response.content))
img.save(filename)
img = ""
