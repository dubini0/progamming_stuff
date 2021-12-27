n = int(input())

n_list = list(map(int, input().split()))
max_value = max(n_list)

sum = 0
for i in range(len(n_list)):
    sum += n_list[i]

result = (100*sum)/(len(n_list)*max_value)
print(result)
