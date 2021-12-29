alpha = "abcdefghijklmnopqrstuvwxyz"
result = [-1]*26

s_list = list(map(str, input()))
# print(s_list)


for i in range(len(alpha)):
    try:
        idx = s_list.index(alpha[i])
        result[i] = idx
    except:
        continue

for i in result:
    print(i, end=" ")
print()
