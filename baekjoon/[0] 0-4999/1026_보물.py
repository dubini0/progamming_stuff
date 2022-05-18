import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a_sorted = sorted(a)
b_sorted = sorted(b, reverse=True)
#print(a_sorted, b_sorted)

res = 0
for i in range(len(a_sorted)):
    res += a_sorted[i] * b_sorted[i]

print(res)
