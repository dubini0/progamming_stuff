n, k = map(int, input().split())

intarr = []
for _ in range(n):
    intarr.append(int(input()))
    
intarr.sort(reverse=True)
sum, cnt = 0, 0
for i in intarr:
    if sum == k:
        break
    if (k-sum) > i:
        q = (k-sum) // i
        sum += i * q
        cnt += q
        
print(cnt)
