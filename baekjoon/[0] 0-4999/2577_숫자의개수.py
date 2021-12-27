a = int(input())
b = int(input())
c = int(input())

num = str(a*b*c)
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(num)):
    result[int(num[i])] += 1

for i in range(len(result)):
    print(result[i])
