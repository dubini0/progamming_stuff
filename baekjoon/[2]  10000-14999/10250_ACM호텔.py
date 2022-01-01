from math import ceil

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    if n%h == 0:
        print("{}{:02d}".format(h, ceil(n/h)))
    else:
        print("{}{:02d}".format(n%h, ceil(n/h)))
