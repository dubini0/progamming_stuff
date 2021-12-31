n = int(input())

for i in range(n):
    print(' '*(n-1-i), end='')
    print('*'*(i+1), end='')
    print()
for i in range(n):
    print(' '*(i+1), end='')
    print('*'*(n-1-i), end='')
    print()
