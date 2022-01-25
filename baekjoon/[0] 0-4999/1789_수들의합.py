import sys

n = int(input())

sum = 0
for i in range(sys.maxsize):
    sum += i
    if sum > n:
        break
    
print(i-1)
