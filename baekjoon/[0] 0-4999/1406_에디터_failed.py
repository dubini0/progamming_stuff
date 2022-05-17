# Note) This code works fine, but it does not satisfy the time limit.
# If you want to see the 'fast' code, see 1406_에디터_.py

import sys

string = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
index = len(string)

for i in range(n):
    args = sys.stdin.readline().split()
    # print(args)
    if args[0] == "P":
        string = string[:index] + args[1] + string[index:]
        index += 1
    elif args[0] == "L":
        if index == 0:
            continue
        else:
            index -= 1
    elif args[0] == "D":
        if index == len(string):
            continue
        else:
            index += 1
    elif args[0] == "B":
        if index == 0:
            continue
        string = string[:index-1] + string[index:]
        index -= 1
    #print(string)

print(string)
