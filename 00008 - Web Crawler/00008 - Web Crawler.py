import bs4 as bs
import urllib.request
import csv
import requests
from PIL import Image
from io import BytesIO
import os
import pandas as pd


def CreateFolder(folder_name):
    try:
        os.mkdir(folder_name)
    except OSError:
        print ("Creation of the directory '%s' failed, the file already exist" % folder_name)


def DownloadImage(url,filename,ext = "png"):
    createFolder(("downloads"))
    output_filename = filename + "." + ext
    urllib.request.urlretrieve(url, output_filename)
    response = requests.get(url)
    name = f"test.png"
    filename = f"./downloads/{name}"
    img = Image.open(BytesIO(response.content))
    img.save(filename)
    img = ""


def OutputHTMLFileSummary(url,html_tag,output_file):
    a = []
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    # print(soup.encode("utf-8"))
    f = csv.writer(open(output_file, "w", encoding="utf-8"))
    links = soup.find_all(html_tag)
    for link in links:
        print(link)
        if link == a:
            pass
        else:
            try:
                f.writerow([link.name,link.a,link.a.next_sibling,str(link)])
            except:
                f.writerow([link.name,link.a,str(link)])

def OutputHTMLFileSummaryIMG(url,html_tag,output_file):
    a = []
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    # print(soup.encode("utf-8"))
    f = csv.writer(open(output_file, "w", encoding="utf-8"))
    links = soup.find_all(html_tag)
    for link in links:
        print(link)
        if link == a:
            pass
        else:
            f.writerow([link.name, link.title, link["src"], link.text, str(link)])

url1 = 'https://yugioh.fandom.com/wiki/Set_Card_Lists:Deck_Build_Pack:_Mystic_Fighters_(OCG-JP)'
url2 = 'https://yugioh.fandom.com/wiki/Set_Card_Galleries:Deck_Build_Pack:_Mystic_Fighters_(OCG-JP)'

html_tag = "tr"
output_file1 = "DBMF - CardList - tr.csv" #change this to your own file output
output_file2 = "DBMF - CardGallery - img.csv" #change this to your own file output
output_file3 = "DBMF - CardGallery - img2.csv" #change this to your own file output
output_file4 = "DBMF - CardList - a.csv" #change this to your own file output


# source = urllib.request.urlopen(url).read()
# soup = bs.BeautifulSoup(source,'lxml')
# print(soup.encode("utf-8"))
# # links = soup.find_all(html_tag, id=False)
# links = soup.find_all(html_tag)
#
# for link in links:
#     print(link.name,link.text)

# OutputHTMLFileSummary(url1,"tr",output_file1)
# OutputHTMLFileSummary(url2,"img",output_file2)
# OutputHTMLFileSummaryIMG(url2,"img",output_file3)
OutputHTMLFileSummary(url2,"a",output_file4)





