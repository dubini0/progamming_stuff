n = int(input())

cnt = 0
for i in range(n):
    string = input()
    str_list = [string[0]]
    prev = string[0]
    flag = 0

    for s in string:
        if s == prev:
            continue
        else:
            prev = s
            if s in str_list:
                flag = 1
                break
            str_list.append(s)
            
    if flag == 1:
        continue
    cnt += 1

print(cnt)
