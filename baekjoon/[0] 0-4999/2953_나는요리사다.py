score = []

for i in range(5):
    score.append(sum(list(map(int, input().split()))))

max_score = max(score)
index = score.index(max_score)

print(index+1, max_score)
