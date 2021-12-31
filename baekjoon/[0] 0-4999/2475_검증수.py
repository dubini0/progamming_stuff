n_list = list(map(int, input().split()))

n_sum = 0
for i in n_list:
    n_sum += i**2

print(n_sum%10)
