from itertools import product
from math import factorial

sm = 4 * len(list(filter(lambda x: x.count('Е') <= 2 and x.count('И') <= 2  and x.count('Я') <= 2, product('ЕИЯ', repeat=6))))
sm += 4 * len(list(filter(lambda x: x.count('Е') <= 2 and x.count('И') <= 2  and x.count('Я') <= 2, product('ЕИЯ', repeat=5))))
sm += 4 * (len(list(filter(lambda x: x.count('Е') <= 2 and x.count('И') <= 2  and x.count('Я') <= 2, product('ЕИЯ', repeat=4)))))
sm += 4 * (len(list(filter(lambda x: x.count('Е') <= 2 and x.count('И') <= 2  and x.count('Я') <= 2, product('ЕИЯ', repeat=3)))))
sm += 3 * (len(list(filter(lambda x: x.count('Е') <= 2 and x.count('И') <= 2  and x.count('Я') <= 2, product('ЕИЯ', repeat=2)))))
print(sm)
print(len(list(filter(lambda x: x.count('Е') <= 2 and x.count('И') <= 2  and x.count('Я') <= 2, product('ЕИЯ', repeat=6)))))
print(factorial(6) // 2 // 2 // 2)
print(factorial(5) // 2 // 2 // 1 * 3)