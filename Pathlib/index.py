import os


folder = "HS"

for key, value in enumerate(os.listdir(folder)):
    print({key: value})
    
    y = f"{folder}/{value}"
    z = f"{folder}/hotel-{key}.jpeg"

    os.rename(y, z)




for i in os.listdir():
    if "siyamak.py" in i:
        old = "siyamak.py"
        new = "sort.py"
        os.rename(old, new)
    else:
        print(False)



# --------------------------------------------------


# remove a dir that has files contained in it
import shutil
for key , value in enumerate(os.listdir()):
    print(key, value)

    old = ".vscode"
    new = ".siyamak"
    shutil.rmtree(new)

# -----------------------------------------
import pathlib

print(dir(pathlib))
print(pathlib.WindowsPath)
print(pathlib.__name__)
print(pathlib.__loader__)
print(pathlib.io)
print(pathlib.sys)

# -----------------------------------------------
import pathlib

print(pathlib.Path.home()) #/home/siyamak
print(pathlib.Path.cwd()) #/home/siyamak/Documents/Algoritem

# -------------------------------------------------

print(os.path.join(os.getcwd()))
print(os.path.join(os.path.join(os.getcwd(), 'in'), 'out.py')) #/home/siyamak/Documents/Algoritem/in/out.py
print(pathlib.Path.cwd().joinpath('in').joinpath('out.py')) #/home/siyamak/Documents/Algoritem/in/out.py

if (pathlib.Path.cwd()).is_dir():
    print(True)
else:
    print(0)

if os.path.join(os.getcwd()) == pathlib.Path.cwd():
    print(True)
else:
    print(0)

# ----------------------------------------------------
# copule of folder is created
count = 0
for i in range(10):
    os.mkdir(os.path.join(os.getcwd(), f"siyamak{count}"))
    count += 1

# -----------------------------------------------------
# move to new directory

newpath = "/home/siyamak/Download"
for i in os.listdir():
    shutil.move(i, newpath)


