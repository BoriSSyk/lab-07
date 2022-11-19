n = int(input('N рядки -'))
a = []
m = 0
for _ in range(n):
    word = input()
    a.append(word)
    m = max(m, len(word))
for word in a:
    print(word.ljust(m, '*'))
