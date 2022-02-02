n = int(input())

vote = input()
a_cnt, b_cnt = 0, 0
for i in vote:
    if i == "A":
        a_cnt += 1
    elif i == "B":
        b_cnt += 1
        
if a_cnt > b_cnt:
    result = "A"
elif a_cnt < b_cnt:
    result = "B"
else:
    result = "Tie"

print(result)
