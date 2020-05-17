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
url1 = 'https://yugioh.fandom.com/wiki/Set_Card_Lists:Deck_Build_Pack:_Mystic_Fighters_(OCG-JP)'
# url2 = 'https://yugioh.fandom.com/wiki/Set_Card_Galleries:Deck_Build_Pack:_Mystic_Fighters_(OCG-JP)'
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

# with open(output_file1,"r",encoding="utf-8") as in_file:
#     with open(output_file1_2, 'w',encoding="utf-8") as out_file:
#         writer = csv.writer(out_file)
#         for row in csv.reader(in_file):
#             if row:
#                 print(type(row),len(row),row[0])
#                 new_row = row[0].replace("<a>",",")
#                 print(new_row)



def OutputHTMLFileSummary2(url,html_tag,output_file):
    array = []
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'html.parser')
    f = csv.writer(open(output_file, "w", encoding="utf-8"))
    links = soup.find_all(html_tag)

    counter = 0.0
    for link in links:
        counter += 1
        if (counter/2) != 0.0:
            array.append([f.text.strip().replace("\xa0\n\t", "") for f in link.find_all("td")])
            print(counter)
        else:
            pass
    print(array)
    for i in range(len(array)):
        f.writerow([array[i]])
    df = pd.DataFrame()
    df["Data"] = array
    return df
df = OutputHTMLFileSummary2(url1,"tr",output_file6)
df = df.drop([0])
df = df.replace({'[':''}, regex=True)
# print(df)
# for i in range(len(df)):
#     df.iloc[i] = df.iloc[i].replace("[","")
#     df.iloc[i] = df.iloc[i].replace("]","")
#     print(df.iloc[i])


df.count
df.to_csv("output.csv",index = False)
with open("output.csv","r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        new_row = row[0].replace("[","")
        new_row = new_row.replace("]","")
        print(new_row)

