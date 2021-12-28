a, b = map(int, input().split())

new_a, new_b = "", ""
for i in range(len(str(a)), 0, -1):
    new_a += str(a)[i-1]
for i in range(len(str(b)), 0, -1):
    new_b += str(b)[i-1]

if int(new_a) > int(new_b):
    print(new_a)
else:
    print(new_b)
