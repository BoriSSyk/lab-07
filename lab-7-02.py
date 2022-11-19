from random import choice
az = list(map(chr, range(ord('a'), ord('z')+1)))
n = int(input('N= '))
a = [''.join(choice(az) for j in range(n)) for i in range(n)]
print(*a, sep='\n', end='\n\n')
print(max(a, key=lambda x: x.count('o')))
