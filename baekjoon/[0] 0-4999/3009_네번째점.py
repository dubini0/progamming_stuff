x_list, y_list = [], []
for i in range(3):
    a, b = map(int, input().split())
    if a in x_list:
        x_list.remove(a)
    else:
        x_list.append(a)
    
    if b in y_list:
        y_list.remove(b)
    else:
        y_list.append(b)

print(x_list[0], y_list[0])
