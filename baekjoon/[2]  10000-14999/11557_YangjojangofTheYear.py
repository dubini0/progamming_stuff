t = int(input())

for i in range(t):
    n = int(input())
    s_list, l_list = [], []
    for j in range(n):
        tmp = input().split()
        s_list.append(tmp[0])
        l_list.append(int(tmp[1]))
        
    idx = l_list.index(max(l_list))
    print(s_list[idx])
