import sys

stack1 = list(sys.stdin.readline().strip())
stack2 = []
n = int(sys.stdin.readline())

for i in range(n):
    args = sys.stdin.readline().split()
    # print(args)
    if args[0] == "P":
        stack1.append(args[1])
    elif args[0] == "L":
        if stack1:
            stack2.append(stack1.pop())
    elif args[0] == "D":
        if stack2:
            stack1.append(stack2.pop())
    elif args[0] == "B":
        if stack1:
            stack1.pop()
    #print(string)

stack1.extend(reversed(stack2))
print(''.join(stack1))
