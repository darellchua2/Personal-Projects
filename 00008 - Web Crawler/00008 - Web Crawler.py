"""
import bs4 as bs
import urllib.request
import csv

source = urllib.request.urlopen('http://www.bigweb.co.jp/ver2/pd2.php?card_id=3105666').read()


soup = bs.BeautifulSoup(source,'lxml')
print(soup.encode("utf-8"))


f = csv.writer(open("OUTPUT.csv", "w", encoding="utf-8"))

links = soup.find_all('a')

for link in links:
    print(link)
    f.writerow([str(link)])

"""
import urllib
from urllib.request import Request, urlopen
import csv
import requests
from PIL import Image
from io import BytesIO

import io

url = 'https://vignette.wikia.nocookie.net/yugioh/images/5/53/Pikari%40Ignister-IGAS-JP-R.png/revision/latest?cb=20191231105143'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req)
print (webpage.getcode())
print (webpage.read())
print(webpage)

f = csv.writer(open("OUTPUT.csv", "w", encoding="utf-8"))
f.writerow([webpage])

urllib.request.urlretrieve(url, "pic1.png")

response = requests.get(url)
name = f"test.png"
filename = f"./downloads/{name}"
img = Image.open(BytesIO(response.content))
img.save(filename)
img = ""
