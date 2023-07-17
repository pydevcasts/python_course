# print(dir(str))
# print(dir(int))

# x = 125
# print(x.isalnum()) # ham horofe ham adad
# print(x.isalpha())
x = "zahra"
y = "nasim"
# print(x + " " +y)
# print("salam {} hastam va dostam {} hastesh".format(x, y))
# # or 
# print(f"salam man {x} hastam va {y} doste zahra hastam")

name = "zahra riyahi"

# output
# "riyahi zahra"
listname = name.split(" ") #["zahra", "riyahi"]

listname.reverse()
# print(listname)
print("  ".join(listname))