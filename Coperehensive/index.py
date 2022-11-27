first = [2, 3, 4]
second = [20, 30, 40]
final = []
for i in first:
    for j in second:
        final.append(i+j)
print(final)

# in oneline
first = [2, 3, 4]
second = [20, 30, 40]
final = [i+j for i in first for j in second]
print(final)
# [22, 32, 42, 23, 33, 43, 24, 34, 44]
# ==============================================
final = [[x, y] for x in [10, 20, 30] for y in [30, 10, 50] if x != y]
print(final)
# [[10, 30], [10, 50], [20, 30], [20, 10], [20, 50], [30, 10], [30, 50]]
# =============================================