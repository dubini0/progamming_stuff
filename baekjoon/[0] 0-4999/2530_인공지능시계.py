a, b, c = map(int, input().split())
d = int(input())

h, m, s = d // 3600, (d%3600) // 60, d % 60
#print(h, m, s)

s = s+c
if s >= 60:
    s = s % 60
    m += 1

m = m+b
if m >= 60:
    m = m % 60
    h += 1

h = h+a
if h >= 24:
    h = h % 24

print(h, m, s)
