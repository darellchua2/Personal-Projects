import os
import csv
import os.path, time
from datetime import date,datetime,timedelta


import time
start_time = time.time()


today = date.today()


def FileFinder(target_Dir, N = 2):
    with open('File - Summary.csv', 'a', newline='') as output_file:
        ini_time_for_now = datetime.now()
        past_date_before = ini_time_for_now - \
                                 timedelta(days=N)
        writer = csv.writer(output_file)
        writer.writerow(["Today's Date", datetime.now])
        writer.writerow(["Date of Check", past_date_before, "Last Modified"])
        writer.writerow(["File Path", "Created On", "Last Modified", "File Size (MB)"])
        for subdir, dirs, files in os.walk(target_Dir):
            for file in files:
                filepath = subdir + os.sep + file
                last_modified = os.path.getmtime(filepath)
                created = os.path.getctime(filepath)
                file_size = os.path.getsize(filepath)/(1024.0*1024.0)
                if past_date_before <= datetime.fromtimestamp(last_modified):
                    # print(filepath, time.ctime(last_modified),time.ctime(created))
                    writer.writerow([filepath,time.ctime(created), time.ctime(last_modified), file_size])



# target_Dir = input("Please input the Root Folder you want to search from: ")

target_Dir1 = "S:\\Projects\\Proposal\\LTA CR116"
target_Dir2 = "S:\\Projects\\Proposal\\CR103 (MCC)"
target_Dir3 = "S:\\Projects\\Proposal\\KTC PE_JTC_Infrastructure Works_Bulim Phase 2"


FileFinder(target_Dir1)
FileFinder(target_Dir2)
FileFinder(target_Dir3)



print("This has completed")
print("--- %s seconds ---" % (time.time() - start_time))

