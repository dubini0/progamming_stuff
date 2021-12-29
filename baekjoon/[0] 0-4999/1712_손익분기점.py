a, b, c = map(int, input().split())

if c-b <= 0:
    print(-1)
else:
    x = a // (c-b)
    print(x+1)
