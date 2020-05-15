import os
import csv
import os.path, time
from datetime import date,datetime,timedelta
import asyncio

today = date.today()

# def FileFinder(list_dir,loop, N = 2):
#     with open('File - Summary.csv', 'w', newline='') as output_file:
#         ini_time_for_now = datetime.now()
#         past_date_before = ini_time_for_now - \
#                            timedelta(days=N)
#         writer = csv.writer(output_file)
#         writer.writerow(["Today's Date", datetime.now])
#         writer.writerow(["Date of Check", past_date_before, "Last Modified"])
#         writer.writerow(["File Path", "Created On", "Last Modified", "File Size"])


async def FileFinder(list_dir,loop, N = 2):
    with open('File - Summary.csv', 'w', newline='') as output_file:
        ini_time_for_now = datetime.now()
        past_date_before = ini_time_for_now - \
                           timedelta(days=N)
        writer = csv.writer(output_file)
        writer.writerow(["Today's Date", datetime.now])
        writer.writerow(["Date of Check", past_date_before, "Last Modified"])
        writer.writerow(["File Path", "Created On", "Last Modified", "File Size"])
    for target_dir in list_dir:
        asyncio.ensure_future(FileWriteRow(target_dir,N))


async def FileWriteRow(target_Dir,N):
    with open('File - Summary.csv', 'a', newline='') as output_file:
        ini_time_for_now = datetime.now()
        past_date_before = ini_time_for_now - \
                           timedelta(days=N)
        writer = csv.writer(output_file)
        for subdir, dirs, files in os.walk(target_Dir):
            for file in files:
                filepath = subdir + os.sep + file
                last_modified = os.path.getmtime(filepath)
                created = os.path.getctime(filepath)
                file_size = os.path.getsize(filepath) / (1024.0 * 1024.0)
                if past_date_before <= datetime.fromtimestamp(last_modified):
                    print(filepath, time.ctime(last_modified), time.ctime(created))
                    writer.writerow([filepath, time.ctime(created), time.ctime(last_modified), file_size])
            await asyncio.sleep(1)


    print("This has completed")
    input("Press Enter to Exit")

# target_Dir = input("Please input the Root Folder you want to search from: ")

target_Dir1 = "S:\\Projects\\Proposal\\LTA CR103"
target_Dir2 = "S:\\Projects\\Proposal\\CR103 (MCC)"
list_dir = [target_Dir1,target_Dir2]

loop = asyncio.get_event_loop()
loop.run_until_complete(FileFinder(list_dir,loop))



