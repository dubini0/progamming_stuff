
input_list = []
for i in range(9):
    input_list.append(int(input()))

find = sum(input_list) - 100
for i in range(len(input_list)-1):
    for j in range(i+1, len(input_list)):
        # print(i, j)
        if (input_list[i] + input_list[j]) == find:
            a, b = input_list[i], input_list[j]
            input_list.remove(a)
            input_list.remove(b)
            break

input_list.sort()
for i in input_list:
    print(i)
