n_list=[]

for i in range(9):
    n_list.append(int(input()))

max_value = max(n_list)
print(max_value)
print(n_list.index(max_value)+1)
