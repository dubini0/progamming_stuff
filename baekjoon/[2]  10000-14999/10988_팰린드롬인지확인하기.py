test = input()

while len(test):
    if len(test) == 1:
        break
    
    if test[0] == test[-1]:
        test = test[1:-1]
        #print(test)
    else:
        print('0')
        exit()
print('1')
