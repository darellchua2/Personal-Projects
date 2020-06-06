# import os
# import csv
# import os.path, time
# from datetime import date,datetime,timedelta
# import asyncio
#
# today = date.today()
#
# def FileCreate(N = 2):
#     with open('File - Summary.csv', 'w', newline='') as output_file:
#         ini_time_for_now = datetime.now()
#         past_date_before = ini_time_for_now - \
#                            timedelta(days=N)
#         writer = csv.writer(output_file)
#         writer.writerow(["Today's Date", datetime.now])
#         writer.writerow(["Date of Check", past_date_before, "Last Modified"])
#         writer.writerow(["File Path", "Created On", "Last Modified", "File Size"])
#
#
# async def FileFinder(list_dir,loop, N = 2):
#     for target_dir in list_dir:
#         asyncio.ensure_future(FileWriteRow(target_dir,N))
#
#
# async def FileWriteRow(target_Dir, N = 2):
#     with open('File - Summary.csv', 'a', newline='') as output_file:
#         ini_time_for_now = datetime.now()
#         past_date_before = ini_time_for_now - \
#                                  timedelta(days=N)
#         writer = csv.writer(output_file)
#         for subdir, dirs, files in os.walk(target_Dir):
#             for file in files:
#                 filepath = subdir + os.sep + file
#                 last_modified = os.path.getmtime(filepath)
#                 created = os.path.getctime(filepath)
#                 file_size = os.path.getsize(filepath)/(1024.0*1024.0)
#                 if past_date_before <= datetime.fromtimestamp(last_modified):
#                     print(filepath, time.ctime(last_modified),time.ctime(created))
#                     writer.writerow([filepath,time.ctime(created), time.ctime(last_modified), file_size])
#                     await asyncio.sleep(1)
#
#     print("This has completed")
#     input("Press Enter to Exit")
#
# # target_Dir = input("Please input the Root Folder you want to search from: ")
# #
# target_Dir1 = "S:\\Projects\\Proposal\\LTA CR103"
# target_Dir2 = "S:\\Projects\\Proposal\\CR103 (MCC)"
# list_dir = [target_Dir1,target_Dir2]
#
# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(FileFinder(list_dir,loop))
#
# FileCreate()
# async def main(target_Dir1,target_Dir2):
#     # Schedule three calls *concurrently*:
#     await asyncio.gather(
#         FileWriteRow(target_Dir1, 2),
#         FileWriteRow(target_Dir2, 2),
#     )
#
# asyncio.run(main(target_Dir1,target_Dir2))


import os
import csv
import os.path, time
from datetime import date,datetime,timedelta
import asyncio

import time
start_time = time.time()
today = date.today()

async def FileFinder(target_Dir, N = 2):
    output_file = open('File - Summary.csv', 'a', newline='')
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
                await asyncio.sleep(0)


# target_Dir = input("Please input the Root Folder you want to search from: ")

target_Dir1 = "S:\\Projects\\Proposal\\LTA CR116"
target_Dir2 = "S:\\Projects\\Proposal\\CR103 (MCC)"
target_Dir3 = "S:\\Projects\\Proposal\\KTC PE_JTC_Infrastructure Works_Bulim Phase 2"


async def main(target_Dir1,target_Dir2):
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        FileFinder(target_Dir1, 2),
        FileFinder(target_Dir2, 2),
        FileFinder(target_Dir3, 2),
    )

asyncio.run(main(target_Dir1,target_Dir2))

print("This has completed")
print("--- %s seconds ---" % (time.time() - start_time))


# import asyncio
#
#
#
# async def factorial(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         print(f"Task {name}: Compute factorial({i})...")
#         await asyncio.sleep(1)
#         f *= i
#     print(f"Task {name}: factorial({number}) = {f}")
#
# async def main():
#     # Schedule three calls *concurrently*:
#     await asyncio.gather(
#         factorial("A", 2),
#         factorial("B", 3),
#         factorial("C", 4),
#     )
#
# asyncio.run(main())
#
# # Expected output:
# #
# #     Task A: Compute factorial(2)...
# #     Task B: Compute factorial(2)...
# #     Task C: Compute factorial(2)...
# #     Task A: factorial(2) = 2
# #     Task B: Compute factorial(3)...
# #     Task C: Compute factorial(3)...
# #     Task B: factorial(3) = 6
# #     Task C: Compute factorial(4)...
# #     Task C: factorial(4) = 24
#
#
#
