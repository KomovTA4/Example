from itertools import product, permutations
from math import factorial
# https://stepik.org/lesson/552237/step/9?auth=login&unit=545965
lst1 = sorted(map(lambda x: ''.join(x), permutations('МАРИ', 4)))
lst2 = sorted(map(lambda x: ''.join(x), product('ИНА', repeat=4)))
print(len(lst1), len(lst2))
print()
print(lst1.index('МАРИ') * 81 + lst2.index('АННА') + 1)