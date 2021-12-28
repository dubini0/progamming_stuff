sentence = input().upper()
alphabet_list = list(map(str, sentence))

alphabet_dict = {}
for i in alphabet_list:
    if i in alphabet_dict:
        alphabet_dict[i] += 1
    else:
        alphabet_dict[i] = 1

# print(alphabet_dict)
max_val = max(alphabet_dict.values())
flag = 0
for k, v in alphabet_dict.items():
    if v == max_val:
        result = k
        flag += 1

if flag == 1:
    print(result)
else:
    print('?')
