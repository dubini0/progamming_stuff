
odd = []
for i in range(7):
    tmp = int(input())
    if tmp%2 == 1:
        odd.append(tmp)

if len(odd) == 0:
    print("-1")
else:
    odd.sort()
    print(sum(odd))
    print(odd[0])
