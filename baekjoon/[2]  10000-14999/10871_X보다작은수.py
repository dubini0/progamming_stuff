n, x = input().split()
n, x = int(n), int(x)

n_list = input().split()
n_list = [int(i) for i in n_list]

result = [i for i in n_list if i < x]

for i in range(len(result)):
    print(result[i], end=' ')
