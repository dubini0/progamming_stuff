n_list = []
for i in range(10):
    n_list.append(int(input()))

res_list = [i%42 for i in n_list]
res_set = set(res_list)

print(len(res_set))
