from math import ceil

while True:
    flag = 0
    input_string = input()
    if input_string == "0":
        break
    strlen = len(input_string)
    
    for i in range(ceil(strlen/2), strlen, 1):
        #print(i, strlen-i-1)
        if input_string[i] != input_string[strlen-i-1]:
            flag = 1
            break
    
    if flag == 0:
        print('yes')
    elif flag == 1:
        print('no')
