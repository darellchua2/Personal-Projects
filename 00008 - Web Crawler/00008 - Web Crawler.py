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
# import urllib
# from urllib.request import Request, urlopen
# import csv
# import requests
#
# import io
#
# url = 'https://yugioh.fandom.com/wiki/Set_Card_Galleries:Ignition_Assault_(OCG-JP)?file=TenThousandDragon-IGAS-JP-10000ScR.png'
# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req)
# print (webpage.getcode())
# print (webpage.read())
# print(webpage)
#
# f = csv.writer(open("OUTPUT.csv", "w", encoding="utf-8"))
# f.writerow([webpage])
#
# urllib.request.urlretrieve(url, "pic1.png")
#
# response = requests.get(url)
#
# file = open("sample_image.png", "wb")
# file.write(response.content)
# print(response.content)
# file.close()


import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse

def download(url, pathname):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(buffer_size), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))

def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """
    soup = bs(requests.get(url).content, "html.parser")

def main(url, path):
    # get all images
    imgs = get_all_images(url)
    for img in imgs:
        # for each image, download it
        download(img, path)
