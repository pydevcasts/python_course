# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match




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
# #Return a list containing every occurrence of "ai":
# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)
# ===================================
# #The string property returns the search string:
# txt = "The rain Bin pain"
# x = re.search(r"\bB\w+", txt)
# print(x.string)

###################################################

# #Check if the string starts with "The" and ends with "Spain":
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x.span())
# (0, 17)
########################################
# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)
# output: ['ai', 'ai']
########################################
# txt = "The rain in Spain"
# x = re.findall("Portugal", txt)
# print(x)
# []
#######################################
# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("""The first white-space character
#        is located in position:""", x.start())
# output:3
################################################

# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)
# None
#############################################
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)
# ['The', 'rain', 'in', 'Spain']
################################################

# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)
# ['The', 'rain in Spain']
#############################################
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)
# The9rain9in9Spain
#########################################
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)
# The9rain9in Spain
####################################
# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.span())
# (12, 17)
####################################
# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.string)
# The rain in Spain
##################################
# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.group())
# .group() returns the part of the string where there was a match
#######################################
# txt = "The rAin in Spain"
# #Find all lower case characters alphabetically between "a" and "m":
# x = re.findall("[a-m]", txt)
# print(x)
# # ['h', 'e', 'a', 'i', 'i', 'a', 'i']
#######################################
# txt = "That will be 59 dollars"
# x = re.findall("\d",txt)
# print(x)
#######################################
# txt = "hello planet"
# x = re.findall("he..o", txt)
# print(x)
########################################
# txt = "hello planet"
# #Check if the string starts with 'hello':
# x = re.findall("^hello", txt)
# if x:
#   print("Yes, the string starts with 'hello'")
# else:
#   print("No match")
###################################
# txt = "hello planet"
# #Check if the string ends with 'planet':
# x = re.findall("planet$", txt)
# if x:
#   print("Yes, the string ends with 'planet'")
# else:
#   print("No match")
######################################

# txt = "hello planet"
# x = re.findall("h.*o", txt)
# print(x)
####################################
# txt = "hello planet"
# x = re.findall("h.+o", txt)
# print(x)
####################################
# txt = "The rain in Spain falls mainly in the plain!"
# x = re.findall("falls|norsama", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")
#######################################
txt = "hello planet"
# #Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
# x = re.findall("h.{3}o", txt)
# print(x)
######################################
# x = re.findall("he..?o", txt)
# print(x)
#####################################
# txt = "The rain in Spain"
# #Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
# x = re.findall("\w", txt)
# print(x)
######################################
# txt = "The rain in Spain"
# #Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
# x = re.findall("\w", txt)
# print(x)
####################################
# txt = "The rain@ in Spain"
# #Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
# x = re.findall("\W", txt)
# print(x)
#####################################

# txt = "The rain in Spain"
# #Check if the string starts with "The":
# x = re.findall("\AThe", txt)
# print(x)
###############################
# txt = "The ain in Spain"
#Check if "ain" is present at the beginning of a WORD:
# x = re.findall(r"\bain", txt)
# print(x)
###############################
# txt = "The rain in Spain"
# #Check if "ain" is present at the end of a WORD:
# x = re.findall(r"ain\b", txt)
# print(x)
######################################
# txt = "The rain in Spain"
# #Check if "ain" is present, but NOT at the beginning of a word:
# x = re.findall(r"\Bain", txt)
# print(x)
#####################################
# txt = "The raint in Spain"
# #Check if "ain" is present, but NOT at the end of a word:
# x = re.findall(r"ain\B", txt)
# print(x)
######################################
# txt = "The rain in Spain"
# #Check if the string contains any digits (numbers from 0-9):
# x = re.findall("\d", txt)
# print(x)
########################################
# txt = "The rain in Spain"
# #Return a match at every no-digit character:
# x = re.findall("\D", txt)
# print(x)
# ['T', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 'S', 'p', 'a', 'i', 'n']
########################################
# txt = "The rain in Spain"
# #Return a match at every white-space character:
# x = re.findall("\s", txt)
# print(x)
# [' ', ' ', ' ']
######################################
# txt = "The rain in Spain"
# #Return a match at every NON white-space character:
# x = re.findall("\S", txt)
# print(x)
# ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']
#####################################
# txt = "8 times +before 11:45 AM"
# #Check if the string has any + characters:
# x = re.findall("[8]", txt)
# print(x)
##################################
# txt = "4 times before 11:45 AM"
# #Check if the string has any two-digit numbers, from 00 to 59:
# x = re.findall("[0-5][0-9]", txt)
# print(x)
# ['11', '45']
#####################################
# txt = "The rain12 in Spain"
# #Check if the string has any 0, 1, 2, or 3 digits:
# x = re.findall("[0123]", txt)
# print(x)
# ['1', '2']
####################################
# txt = "The rain in Spain"
# #Check if the string has any a, r, or n characters:
# x = re.findall("[arn]", txt)
# print(x)
# ['r', 'a', 'n', 'n', 'a', 'n']
#######################################
# txt = "The rain in Spain"
# #Check if the string has any characters between a and n:
# x = re.findall("[a-n]", txt)
# print(x)
# ['h', 'e', 'a', 'i', 'n', 'i', 'n', 'a', 'i', 'n']
######################################
# txt = "The rain in Spain"
# #Check if the string has other characters than a, r, or n:
# x = re.findall("[^arn]", txt)
# ['T', 'h', 'e', ' ', 'i', ' ', 'i', ' ', 'S', 'p', 'i']

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
