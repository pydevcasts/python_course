# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# ====================================================
# f = open("demofile.txt", "r")
# print(f.read())

# ====================================

# f = open("demofile.txt", "r")
# print(f.read(5))
# # =================================

# f = open("demofile.txt", "r")
# print(f.readline())

# # ===============================

# f = open("demofile.txt", "r")

# print(f.readline())
# print(f.readline())
# # ===============================
# f = open("demofile.txt", "r")
# for x in f:
#   print(x)
# # ===========================
# f = open("demofile.txt", "r")
# print(f.readline())
# f.close()

# # =============================

# # "x" - Create - will create a file, returns an error if the file exist

# # "a" - Append - will create a file if the specified file does not exist

# # "w" - Write - will create a file if the specified file does not exist
# # ======================================

# f = open("demofile.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())
# # ===============================
# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile3.txt", "r")
# print(f.read())

# ==================================

# import json
# import os
# me = {
#   'name':'siyamak',
#   'family':'abbasnezhad',
#   'age':42
# }
# with open(os.path.join(os.getcwd(),'FileHandling', 'demo.txt'), 'a') as file:
#   json.dump([me], file)

# ==========================================
import csv

# with open("teachers.csv", "a") as csvfile:
#     fieldnames = ['firstname', 'lastname', 'topic']
#     teacherwriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
#     teacherwriter.writeheader()
#     teacherwriter.writerow({
#         "firstname":"siyamak",
#         "lastname":"abasnezhad",
#         "topic":"python"
#     })
with open('teachers.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile)
    rows = list(myreader)
    for row in rows[:]:
        print(', '.join(row))