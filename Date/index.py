import datetime

# x = datetime.datetime.now()
# print(x)


# import calendar
# print(calendar.calendar(2022))

# start = datetime.datetime.now()
# start = start.replace(hour = 9, minute = 8, second = 10, microsecond = 546490)
# print(start)


# worktime = datetime.datetime.now() - start
# print(worktime)

# x = datetime.timedelta(seconds = 12059, microseconds = 41852)
# print(x)




# x = datetime.datetime.now()

# print(x.year)
# print(x.month)
# print(x.day)

# print(x.strftime("%A"))

# =====================================

# x = datetime.datetime(2017, 5, 17)
# print(x)

# =================================


# x = datetime.datetime(2018, 6, 1)

# print(x.strftime("%c"))
# ===========================
# import datetime

# answer_format = '%m/%d'
# link_format = "%b_%d"
# link = 'https://academybime.com/wiki/{}'

# while True:
#     answer = input("What date would you like? Please use the MM/DD format. Enter 'q' to quit.")
#     answer2 = str(answer)
#     if answer2.upper() == 'Q':
#         break

#     try:
#         date = datetime.datetime.strptime(answer, answer_format)
#         output = link.format(date.strftime(link_format))
#         print(output)
#         file = open('output.txt', 'w')
#         file.write(output)
#         file.close()
#     except:
#         print("That's not a valid date. Please try again.")
#         break

# =====================================