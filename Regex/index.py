# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match


# import re


# #Check if the string starts with "The" and ends with "Spain":

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if (x):
#   print("YES! We have a match!")
# else:
#   print("No match")


# d(0,9)
# w(a-z)
# s(space)
# + at least one time
# *
# ^ start
# $ end
# ========================

# import re

# #Return a list containing every occurrence of "ai":

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

# ===================================

# import re

# txt = "The rain in Spain"

# #Check if "Portugal" is in the string:

# x = re.findall("Portugal", txt)
# print(x)

# if (x):
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# =================================


# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print( x.start()) 

# =================================

# import re

# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)
# ========================

# import re

# #Split the string at every white-space character:

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)

# =============================

# import re

# #Split the string at the first white-space character:

# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)
# ============================

# import re

# #Replace all white-space characters with the digit "9":

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)
# =========================

# import re

# #Replace the first two occurrences of a white-space character with the digit 9:

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)
# ==============================

# import re

# #Search for an upper case "S" character in the beginning of a word, and print its position:

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.span())

# ============================
# import re

# #The string property returns the search string:

# txt = "The rain Bin pain"
# x = re.search(r"\bB\w+", txt)
# print(x.string)
# =============================

# import re

# #Search for an upper case "S" character in the beginning of a word, and print the word:

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.group())

