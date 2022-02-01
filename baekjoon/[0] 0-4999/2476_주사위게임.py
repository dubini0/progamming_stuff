n = int(input())

result = []
for i in range(n):
    res = 0
    n_list = list(map(int, input().split()))
    if (len(set(n_list)) == 1):
        res = 10000 + n_list[0] * 1000
    elif (len(set(n_list)) == 3):
        res = max(n_list) * 100
    else:
        if n_list[1] == n_list[2]:
            res = 1000 + n_list[1] * 100
        else:
            res = 1000 + n_list[0] * 100
    result.append(res)
        
print(max(result))
