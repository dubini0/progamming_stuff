t = int(input())

for i in range(t):
    n, d = map(int, input().split())
    sum = 0
    for j in range(n):
        v, f, c = map(int, input().split())
        time = d / v
        if time <= (f / c):
            sum += 1
    print(sum)
