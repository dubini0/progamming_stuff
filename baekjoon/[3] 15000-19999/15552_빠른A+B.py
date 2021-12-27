import sys

n = int(input())

for i in range(n):
    a, b = sys.stdin.readline().rstrip().split(' ')
    a, b = int(a), int(b)

    print(a+b)
