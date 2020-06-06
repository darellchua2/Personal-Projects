import os
import csv
import win32con, win32api

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

target_Dir = input("Please input the Root Folder you want to search from: ")
target_file_extension = input("Source File Extension that you want to delete in the following format (e.g - .bak):").lower()
reference_file_extension_to_match = input(" Ref File Extension in the following format (e.g - .dwg):").lower()
isDel = input("Do you want to delete found files? Key in 'True' for delete, 'False' for dont delete: ")

FileFinder(target_Dir, target_file_extension, reference_file_extension_to_match,isDel)



