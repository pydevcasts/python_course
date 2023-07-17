first = [2, 3, 4]
second = [20, 30, 40]
# final = []
# for i in first:
#     for j in second:
#         final.append(i+j)
# print(final)
# ================================
# in oneline
# first = [2, 3, 4]
# second = [20, 30, 40]
# print([i+j for i in first for j in second])
# print(final)
# [22, 32, 42, 23, 33, 43, 24, 34, 44]
# # ==============================================
# final = [[x, y] for x in [10, 20, 30] for y in [30, 10, 50] if x != y]
# print(final)
# # [[10, 30], [10, 50], [20, 30], [20, 10], [20, 50], [30, 10], [30, 50]]
# # =============================================
# col = range(10)
# row = range(4)
# final = [(x, y) for x in col for y in row]
# print(final)
# ======================================
# zahra = {number:letter for letter, number in zip("zahrariyahi", range(1,10))}
# print(zahra)
# ==========================================
# total = range(1,100)
# fizzbuzz = {
#     "fizz":[i for i in total if i % 3 == 0],
#     "buzz":[i for i in total if i % 2 == 0]
# }
# print(fizzbuzz)
# ======================================
d = [round(x/y) for y in range(1,10) for x in range(1,9)]
print(d)
