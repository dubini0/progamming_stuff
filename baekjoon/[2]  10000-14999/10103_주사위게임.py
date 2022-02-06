cy, sd = 100, 100

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        sd -= a
    elif b > a:
        cy -= b
    else:
        continue
    
print(cy)
print(sd)
