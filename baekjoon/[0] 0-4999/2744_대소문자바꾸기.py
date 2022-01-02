input_list = list(map(str, input()))

for i in input_list:
    if 64 < ord(i) and ord(i) < 91:
        print(chr(ord(i)+32), end='')
    elif 96 < ord(i) and ord(i) < 123:
        print(chr(ord(i)-32), end='')
print()
