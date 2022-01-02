dices = list(map(int, input().split()))

count = [0, 0, 0, 0, 0, 0]
for i in dices:
    count[i-1] += 1

idx = max(count)
if idx == 1:
    result = max(dices)*100
elif idx == 2:
    result = 1000 + (count.index(idx)+1)*100
elif idx == 3:
    result = 10000 + (count.index(idx)+1)*1000
print(result)
