from math import ceil

a, b, v = map(int, input().split())

v = v - a
result = ceil(v / (a-b))

print(result+1)
