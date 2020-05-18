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
    soup = bs.BeautifulSoup(source, 'html.parser')
    # print(soup.encode("utf-8"))
    f = csv.writer(open(output_file, "w", encoding="utf-8"))
    links = soup.find_all(html_tag)
    counter = 0.0
    for link in links:
        counter +=1
        print(link)
        f.writerow([str(link)])

def OutputHTMLFileSummaryIMG(url,html_tag,output_file):
    a = []
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'html.parser')
    # print(soup.encode("utf-8"))
    f = csv.writer(open(output_file, "w", encoding="utf-8"))
    links = soup.find_all(html_tag)
    for link in links:
        print(link)
        if link == a:
            pass
        else:
            f.writerow([link.name, link.title, link["src"], link.text, str(link)])
    f.close()
url1 = 'https://yugipedia.com/wiki/Set_Card_Lists:Deck_Build_Pack:_Mystic_Fighters_(OCG-JP)'
url2 = 'https://yugipedia.com/wiki/Set_Card_Galleries:Deck_Build_Pack:_Mystic_Fighters_(OCG-JP)'
#
# html_tag = "tr"
output_file1 = "DBMF - CardList - tr1.csv" #change this to your own file output
# output_file2 = "DBMF - CardGallery - img.csv" #change this to your own file output
# output_file3 = "DBMF - CardGallery - img2.csv" #change this to your own file output
# output_file4 = "DBMF - CardList - a.csv" #change this to your own file output
# output_file5 = "DBMF - CardList - td.csv" #change this to your own file output
output_file6 = "DBMF - CardList - tr1.csv" #change this to your own file output

#
#
#
# # source = urllib.request.urlopen(url).read()
# # soup = bs.BeautifulSoup(source,'lxml')
# # print(soup.encode("utf-8"))
# # # links = soup.find_all(html_tag, id=False)
# # links = soup.find_all(html_tag)
# #
# # for link in links:
# #     print(link.name,link.text)
#
# OutputHTMLFileSummary(url1,"tr",output_file1)
# # OutputHTMLFileSummary(url2,"img",output_file2)
# # OutputHTMLFileSummaryIMG(url2,"img",output_file3)
# OutputHTMLFileSummary(url2,"a",output_file4)
# OutputHTMLFileSummary(url2,"td",output_file5)

output_file1_2 = "DBMF - CardList - tr2.csv" #change this to your own file output


def OutputCardList(url,html_tag,output_file):
    lists = []
    counter = 0
    df = pd.DataFrame(columns = ("CODE","Card Name","Card Name(Japanese)", "Rarity","Card Type","Status"))
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'html.parser')
    f = csv.writer(open(output_file, "w", encoding="utf-8"))
    links = soup.find_all(html_tag)
    for link in links:
        counter += 1
        # list.append([f.text.strip().replace("\xa0\n\t", "") for f in link.find_all("td")])
        lists.append([f.text.strip().replace("\xa0\n\t", "") for f in link.find_all("td")])
    for i in range(len(lists)):
        print(i)
        if i/2 != 0 and i>1:
            lists[i][1] = lists[i][1].strip('"')
            df.loc[i] = lists[i]
            df.to_csv(output_file6)
    print(df)

OutputCardList(url1,"tr",output_file6)
