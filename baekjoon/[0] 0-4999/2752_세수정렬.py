n_list = list(map(int, input().split()))

n_list.sort()
for i in range(3):
    print(n_list[i], end=' ')
print()
