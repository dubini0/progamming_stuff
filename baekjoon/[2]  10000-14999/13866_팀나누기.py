n_list = list(map(int, input().split()))

n_list.sort()

A = n_list[0] + n_list[3]
B = n_list[1] + n_list[2]

print(abs(A-B))
