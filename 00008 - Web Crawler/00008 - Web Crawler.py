import bs4 as bs
import urllib.request
import csv
import requests
from PIL import Image
from io import BytesIO
import os
import pandas as pd
import re
import time


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





def OutputCardList(url,html_tag,output_file,sub_tag):
    lists = []
    counter = 0
    df = pd.DataFrame(columns = ("CODE","Card Name","Card Name(Japanese)", "Rarity","Card Type"))
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'html.parser')
    f = csv.writer(open(output_file, "w", encoding="utf-8"))
    links = soup.find_all(html_tag)
    for link in links:
        counter += 1
        lists.append([f.text.strip().replace("\xa0\n\t", "") for f in link.find_all(sub_tag)])
    for i in range(len(lists)):
        if i/2 != 0 and i>1 and "NPR":
            if "NPR" in lists[i]:
                pass
            else:
                print(lists[i])
                lists[i][1] = lists[i][1].strip('"')
                df.loc[i] = lists[i]
                df.to_csv(output_file)
    return df


def OutputCardGallery(url,html_tag,output_file,check_string):
    df = pd.DataFrame(columns = ("Card Name","Card URL"))
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'html.parser')
    f = csv.writer(open(output_file, "w", encoding="utf-8"))
    links = soup.find_all(html_tag)
    counter = 0
    for i in range(len(links)):
        print(links[i])
        img_src = links[i]["src"]
        if check_string in img_src:
            img_src = img_src.replace('/thumb','')
            img_src_splitlist = img_src.rsplit('/',2)
            card_name = img_src_splitlist[1].split('-',1)
            card_name[0] = re.sub(r"(\w)([A-Z])", r"\1 \2", card_name[0])
            new_list = [card_name[0],img_src_splitlist[0] + "/" + img_src_splitlist[1]]
            df.loc[counter] = new_list
            counter += 1
    # print(df)
    df.to_csv(output_file)
    return df




def OutputCard(url,html_tag):

    card_names = url.rsplit("/",1)
    card_data = []
    card_data.append(card_names[1])
    counter = 0
    df = pd.DataFrame(columns = ("Card Name","Card Type","Attribute", "Types","Level/Rank/Link","ATK/DEF","Passcode","Lore"))
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'html.parser')
    links = soup.find_all(html_tag)
    for link in links:
        counter += 1
        if len(link.text) != 1:
            print(str(len(link.text)) + " this is " + link.text)
            data = link.text
            data = data.strip('\n')
            card_data.append(data)
    print(len(card_data))
    df.loc[0] = card_data
    df.iloc[0,0] = df.iloc[0,0].replace("_"," ")
    df.to_csv(card_names[1] + ".csv")
    time.sleep(1)
    return df

url1 = 'https://yugipedia.com/wiki/Set_Card_Lists:Gold_Pack_2016_(OCG-JP)'
url2 = 'https://yugipedia.com/wiki/Set_Card_Galleries:Gold_Pack_2016_(OCG-JP)'
#
# html_tag = "tr"
output_file1 = "DBMF - CardList - tr1.csv" #change this to your own file output
output_file2 = "DBMF - Card - MathMech - tr.csv" #change this to your own file output
output_file6 = "DBMF - CardList - tr1.csv" #change this to your own file output
output_file7 = "DBMF - CardGallery - img.csv" #change this to your own file output
output_file1_2 = "DBMF - CardList - tr2.csv" #change this to your own file output
output_file8 = "GP16 - CardList - tr.csv" #change this to your own file output
output_file9 = "GP16 - CardGallery - img.csv" #change this to your own file output


df1 = OutputCardList(url1,"tr",output_file8,"td")
df2 = OutputCardGallery(url2,"img",output_file9,"GP16")

df_new = pd.merge(df1,df2,how = "left", on = ["Card Name"])
df_new.to_csv("GP16 - OVERALL.CSV")
count = df_new["Card URL"]
for value in df_new["Card Name"]:
    value = value.replace(" ","_")
    print(value)


