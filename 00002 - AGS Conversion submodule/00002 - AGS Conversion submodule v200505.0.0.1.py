import os,sys
import csv
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
import shutil
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
      		
#

