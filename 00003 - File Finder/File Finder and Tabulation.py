import os,sys
import csv


target_Dir = "S:\\Projects\\Projects_AC"
print(target_Dir)
with open('Project AC Folder - Summary.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    for subdir, dirs, files in os.walk(target_Dir):
        for file in files:
            base_file, ext = os.path.splitext(file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".bak"):
                for subdir2, dirs2, files2 in os.walk(subdir):
                    for file2 in files2:
                        base_file2, ext2 = os.path.splitext(file2)
                        if base_file == base_file2 and ext2 == ".dwg":
                            file_size = os.path.getsize(filepath)
                            writer.writerow([filepath,file_size])
                            # print(filepath + "|||" + str(file_size))
print("This has completed")




