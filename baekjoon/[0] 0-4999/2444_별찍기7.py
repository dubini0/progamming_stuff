n = int(input())

for i in range(n-1):
    print(" "*(n-i-1), end='')
    print("*"*(i+1), end='')
    print("*"*(i))
    
for i in range(n, 0, -1):
    print(' '*(n-i), end='')
    print('*'*i, end='')
    print('*'*(i-1))
    
