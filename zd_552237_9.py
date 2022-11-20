from itertools import product, permutations
from math import factorial, comb
# https://stepik.org/lesson/552237/step/9?auth=login&unit=545965
lst1 = sorted(permutations(range(0, 16, 2), 6), reverse=True)
lst2 = sorted(permutations(range(1, 16, 2), 6), reverse=True)
i = 0
while i < len(lst1):
    for k in range(5):
        if lst1[i][k] < lst1[i][k + 1]:
            lst1.pop(i)
            break
    else:
        i += 1
i = 0
while i < len(lst2):
    for k in range(5):
        if lst2[i][k] < lst2[i][k + 1]:
            lst2.pop(i)
            break
    else:
        i += 1
# print(len(lst1), len(lst2))
# print(lst1)
# print(lst2)
# print(factorial(6) * comb(8, 2))
cnt = 0
for row1 in lst1:
    for row2 in lst2:
        sr = 0
        row = []
        if row1[0] > row2[0]:
            row = [row1[0], row2[0]]
        else:
            row = [row2[0], row1[0]]
        for k in range(5):
            if row1[k] > row2[k] > row1[k + 1]:
                sr += 1
                row.extend([row1[k + 1], row2[k + 1]])
            elif row2[k] > row1[k] > row2[k + 1]:
                sr -= 1
                row.extend([row2[k + 1], row1[k + 1]])
        if abs(sr) == 5:
            if row[-1] < row[-2]:
                cnt += 1
                print(row)
print(cnt)
