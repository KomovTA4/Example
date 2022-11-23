maxword, minword, word = '', '1'*1000, input()
while word != 'стоп':
    if len(word) > len(maxword):
        maxword = word
    elif len(word) > len(minword):
        minword = word
    word = input()
if set(maxword) & set(minword) == set(minword):
    print('ДА')
else:
    print('НЕТ')