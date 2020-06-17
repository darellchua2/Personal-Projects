import os
import csv
import win32con, win32api
import pandas as pd
import numpy as np

def FileFinder(target_Dir, target_file_extension, reference_file_extension_to_match, isDel = "False"):
    with open('File - Summary.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        for subdir, dirs, files in os.walk(target_Dir):
            for file in files:
                base_file, ext = os.path.splitext(file)
                filepath = subdir + os.sep + file
                if filepath.endswith(target_file_extension):
                    for subdir2, dirs2, files2 in os.walk(subdir):
                        for file2 in files2:
                            base_file2, ext2 = os.path.splitext(file2)
                            if base_file == base_file2 and ext2 == reference_file_extension_to_match:
                                try:
                                    file_size = os.path.getsize(filepath)
                                    writer.writerow([filepath.encode("utf-8"), file_size])
                                    print(filepath + "|||" + str(file_size))
                                    if isDel == "True":
                                        try:
                                            os.remove(filepath)
                                            print(filepath + " has been deleted")
                                        except PermissionError:
                                            print('PermissionError do change')
                                            win32api.SetFileAttributes(filepath, win32con.FILE_ATTRIBUTE_NORMAL)
                                            os.remove(filepath)
                                            writer.writerow([filepath.encode("utf-8"), file_size], "Removed")
                                    elif isDel == "False":
                                        print(filepath + " has not been deleted")
                                except FileNotFoundError:
                                    print(filepath + ' not found')
                                    pass

    print("This has completed")
    input("Press Enter to Exit")

def FileFinder2(target_Dir, target_file_extension):
    dict={}
    l = []
    for subdir, dirs, files in os.walk(target_Dir):
        # print("---")
        # print(subdir)
        currDir = subdir
        for file in files:
            filepath = subdir + os.sep + file
            if file.endswith(target_file_extension):
                filename, file_extension = os.path.splitext(filepath)
                # print(filepath)
                dict["FilePath"] = filepath
                dict["filename"] = file
                dict["subdir"] = subdir
                dict["file_size_bytes"] = os.path.getsize(filepath)
                dict["filename_ent"] = file + ".ent"
                l.append(dict)
                dict = {}
                # print(l)
    # df = pd.DataFrame(l,columns =["FilePath","subdir","filename","filename_ent","file_size_bytes"])
    df = pd.DataFrame(l)
    df["check"] = pd.Series(index = df.index)
    df["directory_that_has_duplicate"] = pd.Series(index = df.index)


    l2 = []
    l3 = []
    for i in range(df.shape[0]):
        for j in range(df.shape[0]):
            subdir_check = df["subdir"][j] + "/ent"
            if df["filename_ent"][i] in df["FilePath"][j] and df["subdir"][i] in subdir_check:
                # print(i,j,type(filepath2))
                check = "Yes"
                directory_that_has_duplicate = df["FilePath"][j]
                # print(i,j,df["FilePath"][j], df["filename_ent"][i])
                break
            else:
                check = "No"
                directory_that_has_duplicate = np.NaN

        l2.append(check)
        l3.append(directory_that_has_duplicate)
        # print(len(l2))
    df["check"] = l2
    df["directory_that_has_duplicate"] = l3




    df.to_csv("interim.csv")
    df2 = df.filter(["FilePath","directory_that_has_duplicate","file_size_bytes"],axis=1)
    df2.replace("")
    print(df2["directory_that_has_duplicate"])
    df2.dropna(subset=["directory_that_has_duplicate"],inplace=True)
    df2.to_csv("summary_2.csv")

    print("This has completed")
    input("Press Enter to Exit")

# target_Dir = input("Please input the Root Folder you want to search from: ")
# target_file_extension = input("Source File Extension that you want to delete in the following format (e.g - .bak):").lower()
# reference_file_extension_to_match = input(" Ref File Extension in the following format (e.g - .dwg):").lower()
# isDel = input("Do you want to delete found files? Key in 'True' for delete, 'False' for dont delete: ")
#
# FileFinder(target_Dir, target_file_extension, reference_file_extension_to_match,isDel)



target_Dir = "S:\Projects\Projects_AC\\18344 ACO N105 (LTA)\BCA SUBMISSION\BCA form"
print(target_Dir)
target_file_extension = ".ent"
FileFinder2(target_Dir, target_file_extension)




