n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(10):
    a, b = map(int, input().split())
    tmp_list = n_list[a-1:b]
    tmp_list.reverse()
    n_list[a-1:b] = tmp_list
    #print(n_list)

for i in n_list:
    print(i, end=' ')
