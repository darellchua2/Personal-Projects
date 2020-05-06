import os,sys
import csv
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
import shutil
import pandas as pd
from csv import DictReader

# 
def CreateFileWithNewExtension(file,destination_folder):
	try: 
		currDir = os.getcwd()
		rootdir = os.path.abspath(os.path.join(currDir, '..'))
		base_file, ext = os.path.splitext(file)
		input_file = rootdir + os.sep + base_file + ".ags"
		output_file = currDir + os.sep + destination_folder + os.sep + base_file + ".csv"
		print(file + " has been copied over to " + destination_folder + " with a change in extension")
		shutil.copyfile(file,output_file)
	except FileExistsError as error:
                    print(file + " File is not copy")
                    pass

def CreateFileWithNewExtension(file,destination_folder,source_extension,destination_extension):
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
	except FileExistsError as error:
                        print(file + " File is not copy")
                        pass

def createFolder(folder_name):
	try:
	    os.mkdir(folder_name)
	except OSError:
	    print ("Creation of the directory %s failed, the file already exist" % folder_name)    

def PrintCSVRowList(row):
	try:
	    print(row[0])
	except IndexError as error:
	    print("There is no index here")

createFolder("AGS TO csv - Compilation")
# CreateFileWithNewExtension(file,"AGS TO csv - Compilation",".ags",".csv")	
currDir = os.getcwd()

for subdir, dirs, files in os.walk(currDir):
    for file in files:
        base_file, ext = os.path.splitext(file)
        filepath = subdir + os.sep + file
        print(filepath)
        if filepath.endswith(".ags"):
        	CreateFileWithNewExtension(file,"AGS TO csv - Compilation",".ags",".csv")


file = "1-SGO_SI_ROM.csv"
file2 = open(file)
reader = csv.reader(file2)
lines = len(list(reader))
# print(lines)


# open file in read mode

csvfile = open("5-SGO SI LIM CHU KANG SINGAPORE.csv", 'r')
csvreader = csv.reader(csvfile)
index = 0
start_index = 0
end_index = 0
new_dict = dict()

for row in csvreader:
	if(start_index == 0):
		print(row)
	if(len(row)==0):
		print(start_index, end_index)
		print("Empty row is at " + str(index))
		end_index = index

		if(start_index == 0):
			new_dict = {"hi2":[start_index,end_index]}
		start_index = index + 1


	index += 1


print(new_dict)