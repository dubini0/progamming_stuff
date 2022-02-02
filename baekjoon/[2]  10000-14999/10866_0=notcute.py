n = int(input())

agree, disagree = 0,0
for i in range(n):
    vote = int(input())
    if vote == 1:
        agree += 1
    else:
        disagree += 1
    
result = "Junhee is cute!" if agree > disagree else "Junhee is not cute!"

print(result)
