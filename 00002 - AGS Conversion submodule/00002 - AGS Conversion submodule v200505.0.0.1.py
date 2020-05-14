import os
import csv
import shutil
import pandas as pd
import asyncio

def FindIndexInCSVToSplit(file):
    index = 0
    start_index = 0
    end_index = 0
    new_dict = {}
    substring = "**"
    max_lines = 0
    with open(file,'r') as f:
        for line in f:
            max_lines +=1
    f.close()
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                if row[0][:2] == substring:
                    store = row[0]
                    start_index = index
                    new_dict[store] = [start_index,end_index]
                elif len(row) ==0 :
                    end_index = index
                    new_dict[store] = [start_index,end_index]
                elif index == max_lines - 1:
                    end_index = index
                    new_dict[store] = [start_index,end_index]
            except IndexError as error:
                    end_index = index
                    new_dict[store] = [start_index,end_index]

            finally: 
                index +=1
    return new_dict




def CreateFileWithNewExtension(file,destination_folder,source_extension = ".ags",destination_extension = ".csv"):
    try: 
        currDir = os.getcwd()
        rootdir = os.path.abspath(os.path.join(currDir, '..'))
        print(currDir)
        print(rootdir)
        base_file, ext = os.path.splitext(file)
        input_file = rootdir + os.sep + base_file + source_extension
        output_file = currDir + os.sep + destination_folder + os.sep + base_file + destination_extension
        print(file + " has been copied over to " + destination_folder + " with a change in extension")
        shutil.copyfile(file,output_file)
        return output_file
    except FileExistsError as error:
                        print(file + " File is not copy")
                        pass

def createFolder(folder_name):
    try:
        os.mkdir(folder_name)
    except OSError:
        print ("Creation of the directory '%s' failed, the file already exist" % folder_name)    

def PrintCSVRowList(row): #not in use
    try:
        print(row[0])
    except IndexError as error:
        print("There is no index here")

def PrepareList(index_dict):
    keys_list = list(index_dict.keys())
    values_list = list(index_dict.values())
    start_index_list = []
    end_index_list = []
    for i in range (0,len(values_list)):
        # print(i,values_list[i][0])
        # print(i,values_list[i][1])
        start_index_list.append(values_list[i][0])
        end_index_list.append(values_list[i][1])
    # print(start_index_list)
    # print(end_index_list)
    return keys_list, start_index_list, end_index_list

def OutputUsableCSV(input_file, output_file):
    df = pd.read_csv(input_file)
    header = df.iloc[0]
    df = df[2:]
    df.rename(columns = header, inplace = True) 
    df.to_csv(output_file,index = False)

def SplitCSVFiles(file): #currently not in use
    base_file, ext = os.path.splitext(file)
    f = open(file, 'r')
    counter = 0
    for a in range(len(start_index_list)):
        output_file = str(base_file) + "-" + str(counter) + ext
        f2 = open(output_file,'w+')
        for b in range(start_index_list[a],end_index_list[a]):
            f2.write(f.readline())
        counter += 1

def SplitCSVFiles(file,outputfile,keys_list,start_index_list, end_index_list):
    base_file, ext = os.path.splitext(file)
    base_file2,ext2 = os.path.splitext(outputfile)
    infile= open(file,'r').readlines()

    for a in range(len(start_index_list)):
        output_file = str(base_file2) + "-" + str(a) + ext
        with open(output_file,'w') as outfile:
            for index,line in enumerate(infile):
                if index >= start_index_list[a] and index <=(end_index_list[a]):
                    outfile.write(line)

def OutputUsableCSV8(input_file, output_file,key_list_value):
    df = pd.read_csv(input_file,header = [1,2])
    print(df.head())
    df.to_csv(output_file,index = False)

def IsCorrectFile(input_file,key_list_value):
    with open(input_file,'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == key_list_value:
                return key_list_value
            else: 
                return ("This is not the right key_list_value: " + key_list_value)


def IsCorrectFile2(input_file,key_list_value):
    with open(input_file,'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == key_list_value:
                return True
            else: 
                return False

def return_contents(file_name):
    with open(file_name) as infile:
        reader = csv.reader(infile)
        return list(reader)

def RemoveCONT(test_file,test_outputfile):
    with open(test_file) as csvfile, open(test_file)  as csvfile_out:
        with open(test_outputfile,'w') as csvfile2:
            csvfile_1 = csvfile.readlines()
            csvfile_2 = csvfile_out.readlines()

            new_list1 = list()
            new_list0 = list()
            isCont = False
            for index,line in enumerate(csvfile_1):
                new_list0 = line.split('","')
                for i in range(len(new_list0)):
                    new_list0[i] = new_list0[i].replace('"','')
                    # print(new_list0[i])

                ref_counter = index + 1
                # print("index is " + str(index))
                line4 = ','.join(new_list0)
                # print(line4)
                for index2,line2 in enumerate(csvfile_2):   
                    new_list1 = line2.split('","')
                    for i in range(len(new_list1)):
                        new_list1[i] = new_list1[i].replace('"','')
                        if(ref_counter == index2):
                            if new_list1[0] == "<CONT>": 
                                isCont = True
                                # print("this index2 is "+ str(index2))
                                # print(str(index) + " OLD (new_list1) = " + str(new_list1))
                                new_list1[0] =""
                                for j in range(len(new_list0)):
                                    # print(new_list0[i])
                                    new_list1[j] = new_list0[j] + new_list1[j]
                                    if j == (len(new_list1) - 1):
                                        new_list1[j] = new_list1[j][2:]
                                
                                # print(str(index) + " NEW (new_list1) = " + str(new_list1))
                                # print(new_list1)
                                line3 = ""
                                for k in range(len(new_list1)):
                                    if k == 0:
                                        line3 = new_list1[k]
                                    elif k == len(new_list1)-1:
                                        line3 = line3 + "," + '"' + new_list1[k]
                                    else:
                                        line3 = line3 + "," + '"' + new_list1[k] + '"'

                                # print(new_list1)
                                # print(i)
                                csvfile2.write(line3)
                        else:
                            pass

                if "<CONT>" in new_list0[0]: 
                    print("this has " + str(new_list0[0]))
                else: 
                    if isCont == True:
                        isCont = False
                        pass
                    else:
                        line2 = ','.join(new_list0)
                        print(new_list0)
                        csvfile2.write(line)

                print("----")

def CreateSubFolder(keys_list,folder_name):
    for key in keys_list:
        new_foldername = folder_name + os.sep + key[2:]
        new_foldername = new_foldername.replace('?','')
        createFolder(new_foldername)    

# def RemoveContentInCell(test_file,test_outputfile,search_keyword = "Unnamed"):
#     with open(test_file) as csvfile:
#         with open(test_outputfile,'w') as csvfile2:
#             csvfile_1 = csvfile.readlines()
#             new_list0,new_list1,new_list2 = list()
#             for index,line in enumerate(csvfile_1):
#                 new_list0 = line.split('","')
#                 for i in range(len(new_list0)):
#                     new_list0[i] = new_list0[i].replace('"','')
#                     if search_keyword in new_list0[i]:
#                         new_list0[i] = "" 



def ReformatHeader(test_file,test_outputfile, content_merge_var = "*",search_keyword = "Unnamed"):
    with open(test_file) as csvfile, open(test_file)  as csvfile_out:
        with open(test_outputfile,'w') as csvfile2:
            csvfile_1 = csvfile.readlines()
            csvfile_2 = csvfile_out.readlines()

            new_list1 = list()
            new_list0 = list()
            new_list2 = list()
            isCont = False
            for index,line in enumerate(csvfile_1):
                new_list0 = line.split('","')
                for i in range(len(new_list0)):
                    new_list0[i] = new_list0[i].replace('"','')
                    if search_keyword in new_list0[i]:
                        new_list0[i] = "" 
                if content_merge_var in new_list0[0] and index == 1: 
                    new_list0[-1] = new_list0[-1].strip()
                    new_list0[-1] = new_list0[-1][:-1]    
                    new_list2 = new_list0

                    # print("this has " + str(new_list0[0]))
                elif content_merge_var in new_list0[0] and index == 2:
                    new_list2 = new_list2 + new_list0
                    for k in range(len(new_list2)):
                        line2 = ','.join(new_list2)
                    csvfile2.write(line2)
                elif index == 3:
                    for k in range(len(new_list2)):
                        line2 = ','.join(new_list2)
                    csvfile2.write(line)
                else: 
                    line2 = ','.join(new_list0)
                    # print(new_list0)
                    csvfile2.write(line)


def CreateUsableCSVToOutput(specific_keylist_values,folder2,folder3):
    for i in range(len(specific_keylist_values)):
        try:
            if IsCorrectFile2(filepath,specific_keylist_values[i]) == True:
                value = specific_keylist_values[i].replace('?','')
                filepath2 = filepath.replace(folder2,(folder2 + os.sep + value[2:]))
                shutil.move(filepath,filepath2)
                filepath3 = filepath2.replace(folder2,folder3)
                print(filepath3)
                print(specific_keylist_values[i])
                OutputUsableCSV8(filepath2,filepath3,specific_keylist_values[i])
                base_file,ext = os.path.splitext(filepath3)
                filepath4 = base_file + "-cleaned1" + ext
                filepath5 = base_file + "-cleaned2" + ext
                RemoveCONT(filepath3,filepath4)
                ReformatHeader(filepath4,filepath5)
                os.remove(filepath4)
                os.remove(filepath3)
                os.remove(filepath2)

        except FileNotFoundError as error:
            pass
        except IndexError as error:
            print(filepath2 + "this file has error")
            

def CombineTable(file1,folder_name = ""):
    file_out = folder_name + os.sep + FindBaseFolderName(folder_name) + " - Combined.csv"
    if file_out == file1:
        print("this is here")
        pass
    else:
        if os.path.isfile(file_out):
            df_out = pd.read_csv(file_out, header = [0])
            df1 = pd.read_csv(file1, header = [0], skiprows = [1])
            result = df_out.append(df1,sort=False)
            result.to_csv(file_out,index = False)
        else:
            df_out = pd.DataFrame()
            df_out.to_csv(file_out,index = False)



def FindBaseFolderName(target_dir):
    return os.path.basename(target_dir)



async def GetFolderList():
    ref_folder = "CSV Cleaning - Compilation"
    currDir = os.getcwd()
    target_dir = currDir + os.sep + ref_folder
    FolderList = list()·
    for subdir, dir,files in os.walk(target_dir):
        if subdir == target_dir:
            pass
        else:
            last_folder_name = os.path.basename(subdir)
            # print(last_folder_name)
            FolderList.append(last_folder_name)
    return FolderList

folder0 = "Source AGS - Compliation"
folder1 = "AGS to CSV - Compilation"
folder2 = "Split CSV - Compilation"
folder3 = "CSV Cleaning - Compilation"
#
# createFolder(folder1)
# createFolder(folder2)
# createFolder(folder3)
#
# currDir = os.getcwd()
# master_keylist = {}
# for subdir, dirs, files in os.walk(currDir):
#     for file in files:
#         base_file, ext = os.path.splitext(file)
#         filepath = subdir + os.sep + file
#         # print(filepath)
#         if filepath.endswith(".ags"):
#             print("This is the file i want to find " + filepath)
#             output_file = CreateFileWithNewExtension(file,folder1,".ags",".csv")
#             index_dict = FindIndexInCSVToSplit(output_file)
#             keys_list, start_index_list, end_index_list = PrepareList(index_dict)
#             CreateSubFolder(keys_list,folder2)
#             CreateSubFolder(keys_list,folder3)
#             output_file2 = output_file.replace(folder1,folder2)
#             SplitCSVFiles(output_file,output_file2,keys_list, start_index_list, end_index_list)
#             master_keylist[base_file] = keys_list
#
# print(master_keylist)
# folder2_dir = currDir + os.sep + folder2
# print("this is folder2_dir path " + folder2_dir)
# for subdir, dirs, files in os.walk(folder2_dir):
#     for file in files:
#         base_file, ext = os.path.splitext(file)
#         filepath = subdir + os.sep + file
#         # print(base_file)
#         if filepath.endswith(".csv"):
#             index_dict = FindIndexInCSVToSplit(filepath)
#             keys_list, start_index_list, end_index_list = PrepareList(index_dict)
#             # print(filepath)
#             specific_keylist_values = list()
#             for master_key in master_keylist:
#                 # print(master_key)
#                 check = base_file.find(master_key)
#                 if check == 0:
#                     # print("yes this is matching file : " + master_key)
#                     specific_keylist_values = master_keylist[master_key]
#                     CreateUsableCSVToOutput(specific_keylist_values,folder2,folder3)


print("Process have completed")


file_out = "Combined.csv"
currDir = os.getcwd()

target_dir1 = currDir + os.sep + folder3 + os.sep + "ISPT"
target_dir2 = currDir + os.sep + folder3 + os.sep + "HOLE"
for subdir,dirs,files in os.walk(target_dir1):
    for file in files:
        filepath = subdir + os.sep + file
        # print(subdir)
        # print(FindBaseFolderName(subdir))
        CombineTable(filepath,subdir)
print(asyncio.run(GetFolderList()))

