import os
import csv
import os.path, time
from datetime import date,datetime,timedelta

today = date.today()

# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False
#
# if is_admin():
#     pass
# else:
#     # Re-run the program with admin rights
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


def FileFinder(target_Dir, N = 2):
    with open('File - Summary.csv', 'w', newline='') as output_file:
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
                    print(filepath, time.ctime(last_modified),time.ctime(created))
                    writer.writerow([filepath,time.ctime(created), time.ctime(last_modified), file_size])


    print("This has completed")
    input("Press Enter to Exit")

# target_Dir = input("Please input the Root Folder you want to search from: ")

target_Dir = "S:\\Projects\\Proposal\\LTA CR116\\"


FileFinder(target_Dir)



