import os,sys
import csv
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
import shutil
import pandas as pd
from csv import DictReader

def FindIndexInCSVToSplit(file):
	index = 0
	start_index = 0
	end_index = 0
	new_dict = {}
	substring = "**"
	with open(file) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			try:
				if substring in row[0]:
					store = row[0]
					start_index = index
					# print("this is start index " + str(start_index))
			except IndexError as error:
				# print("Empty row is at " + str(index))
				end_index = index
				new_dict[store] = [start_index,end_index]
			finally: 
				index +=1
	return new_dict

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

def PrepareList(index_dict):
	keys_list = list(index_dict.keys())
	values_list = list(index_dict.values())
	start_index_list = []
	end_index_list = []
	for i in range (0,len(values_list)):

		print(i,values_list[i][0])
		print(i,values_list[i][1])
		start_index_list.append(values_list[i][0])
		end_index_list.append(values_list[i][1])

	print(start_index_list)
	print(end_index_list)
	return keys_list, start_index_list, end_index_list

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



index_dict = FindIndexInCSVToSplit("5-SGO SI LIM CHU KANG SINGAPORE.csv")



keys_list, start_index_list, end_index_list = PrepareList(index_dict)

index = 0
dict_index = 0
# with open("5-SGO SI LIM CHU KANG SINGAPORE.csv") as csvfile:
# 		reader = csv.reader(csvfile)
# 		for row in reader:
# 			try:
# 				if keys_list[dict_index] == row[index]:
# 					print("this is the right key index " + str(keys_list[index]))
# 					dict_index += 1
# 				else:
# 					pass
# 			except IndexError as error:
# 				index +=1
