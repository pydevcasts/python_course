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
# D not number
# w(a-z A-Z 0-9)
# W except unicode
# s(space)
# + at least one time happen
# * at least 0 time happen
# ^ start
# $ end
# B not boundry
# b boundry
# ========================

import re

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

# print(x.start()) 

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

#Split the string at the first white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
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

#################################################################
# regex => regular expression
import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

# print(data)
last_name = r'Abasnezhad'
first_name = r'Siyamak'
# print(re.match(last_name, data))
# print(re.search(first_name, data))
# out
# <re.Match object; span=(0, 10), match='Abasnezhad'>
# <re.Match object; span=(12, 19), match='Siyamak'>

# #####################################################33
# \w -> a-z, A-Z, 0-9, _
# \W -> except unicode

# \s -> white space
# \S -> not white space

# \D -> not number
# \d -> number 0-9

# \B -> Not boundry
# \b -> boundry

### print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))
# out:

# 
# {3} -> repeat 3 times
# {,3} -> repeat 0 - 3 times
# {3, 5} -> 3, 4, 5 times

# generic

# ? -> optional
# * -> at least 0 time happen
# + -> at least 1 time happen

### print(re.findall(r'\w*, \w+', data))
# out:
# ['Abasnezhad, Siyamak', 'Teacher, poing', 'McFarland, Dave',
#  'Teacher, poing', 'Arthur, King', 'King, Camelot', 'Österberg,
#  Sven', 'Governor, Norrbotten', ', Tim', 'Enchanter, Killer',
#  'Carson, Ryan', 'CEO, poing', 'Doctor, The', 'Lord, Gallifrey',
#  'Exampleson, Example', 'Example, Example', 'Hassan, Rohani', 
# 'President, Iran', 'Chalkley, Andrew', 'Teacher, poing', 'Vader,
#  Darth', 'Lord, Galactic', 'Sanz, María', 'Minister, Spanish']
# ##########################################################333
# print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
# out:
# ['(555) 555-5555', '(555) 555-5554', '(555) 555-5543',
#  '555-555-5552', '555 555-5551', '(555) 555-5553', '(555) 555-4444']
###################################################
# set -> []

# [aple] -> apple
# [a-z]  -> all small characters
# [A-Z]  -> all capital characters
# [^2]   -> except something

# print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
# out:
# ['Siyamak@poing.com', 'dave@poing.com', 'king_arthur@camelot.co.uk',
# 'governor@norrbotten.co.se', 'tim@killerrabbit.com', 'ryan@poing.com',
#  'doctor+companion@tardis.co.uk', 'me@example.com',
#  'president@ir.gov', 'andrew@poing.com', 'darth-vader@empire.gov', 'mtfvs@spain.gov']
###############################################################################
# print(re.findall(r'\b[poing]{7}\b', data, re.I))
# print(re.findall(r'''
# \b@[-\w\d.]* # First a word boundry, an @, and then any number of characters
# [^gov\t]+ # Ignore 1+ instances of the letters 'g', 'o' or 'v' and a tab
# \b #match another word boundry

# ''', data, re.VERBOSE | re.I))

# print(re.findall(r"""
# \b[\w]+, # Find a word boundry, 1+ hyphens or characters and a comma
# \s       # Find 1 white space
# [-\w ]+  # 1+ hyphen and character and explicit spaces
# [^\t\n]  # Ignore tabs and new lines
# """, data, re.X))

line = re.compile(r''' 
^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t # last name and first name
(?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone
(?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
(?P<instagram>@[\w\d]+)?$ # Instagram
''', re.X | re.M)


# print(re.search(line, data).groupdict())
# out:
# {'name': 'Abasnezhad, Siyamak', 'last': 'Abasnezhad','first': 'Siyamak', 
#  'email': 'Siyamak@poing.com',
#  'phone': '(555) 555-5555', 'job': 'Teacher, poing\t',
#   'instagram': '@SiyamakAbasnezhad'}
#   ###################################################
for match in line.finditer(data):
    print(match.group('name'))
    print('{first}  {last} <{email}>'.format(**match.groupdict()))
#############################################################


# out:
# Abasnezhad, Siyamak
# Siyamak  Abasnezhad <Siyamak@poing.com>
# McFarland, Dave
# Dave  McFarland <dave@poing.com>
# Arthur, King
# King  Arthur <king_arthur@camelot.co.uk>
# Österberg, Sven-Erik
# Sven-Erik  Österberg <governor@norrbotten.co.se>
# , Tim
# Tim   <tim@killerrabbit.com>
# Carson, Ryan
# Ryan  Carson <ryan@poing.com>
# Doctor, The
# The  Doctor <doctor+companion@tardis.co.uk>
# Exampleson, Example
# Example  Exampleson <me@example.com>
# Hassan, Rohani
# Rohani  Hassan <president@ir.gov>
# Chalkley, Andrew
# Andrew  Chalkley <andrew@poing.com>
# Vader, Darth
# Darth  Vader <darth-vader@empire.gov>
# Fernández de la Vega Sanz, María Teresa
# María Teresa  Fernández de la Vega Sanz <mtfvs@spain.gov>