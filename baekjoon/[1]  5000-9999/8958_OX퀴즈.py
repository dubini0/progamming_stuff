n = int(input())

for i in range(n):
    prob = input()
    points, sum = 0, 0
    for j in range(len(prob)):
        if prob[j] == 'O':
            points += 1
            sum += points
        else:
            points = 0
        #print(f"{points}, {sum}")
    print(sum)
