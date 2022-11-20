cnt = int(input())
frase = [chr(index) for index in range(ord('A'), ord('A') + cnt)]
for k in range(cnt, 0, -1):
    for ch in frase:
        print(ch + str(k), end=' ')