import os
# # -----------------------------------------
import pathlib

# folder = "HS"

# for key, value in enumerate(os.listdir(folder)):
#     print({key: value})
    
#     y = f"{folder}/{value}"
#     z = f"{folder}/masjed-{key}.html"

#     os.rename(y, z)




# for i in os.listdir():
#     if "siyamak.py" in i:
#         old = "siyamak.py"
#         new = "sort.py"
#         os.rename(old, new)
#     else:
#         print(False)

# =====================================
# x = [1,2,6,5,8]
# for i in x:
#     if i == 5:
#         break
#     else:
#         print(i) 

# # --------------------------------------------------


# remove a dir that has files contained in it
# import shutil
# for key , value in enumerate(os.listdir()):
#     new = "HS"
#     shutil.rmtree(new)
#     break



# print(dir(pathlib))
# print(pathlib.WindowsPath)
# print(pathlib.__name__)
# print(pathlib.__loader__)
# print(pathlib.io)
# print(pathlib.__file__)

# # -----------------------------------------------
# import pathlib

# print(pathlib.Path.home()) #/home/siyamak
# print(pathlib.Path.cwd()) #/home/siyamak/Documents/Algoritem

# # -------------------------------------------------

# print(os.path.join(os.getcwd()))
# print(os.path.join(os.path.join(os.getcwd(), 'in'), 'out.py')) #/home/siyamak/Documents/Algoritem/in/out.py
# print(pathlib.Path.cwd().joinpath('in').joinpath('out.py')) #/home/siyamak/Documents/Algoritem/in/out.py

# if (pathlib.Path.cwd()).is_dir():
#     print(True)
# else:
#     print(0)

# if os.path.join(os.getcwd()) == pathlib.Path.cwd():
#     print(True)
# else:
#     print(0)

# # ----------------------------------------------------
# # copule of folder is created
# count = 0
# for i in range(5):
#     os.mkdir(os.path.join(os.getcwd(), f"siyamak{count}"))
#     count += 1

# # -----------------------------------------------------
# # move to new directory

# newpath = "/home/siyamak/Download"
# for i in os.listdir():
#     shutil.move(i, newpath)


# ============================


# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")
