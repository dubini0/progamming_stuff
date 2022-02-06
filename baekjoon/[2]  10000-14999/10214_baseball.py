n = int(input())

for i in range(n):
    y_score, k_score = 0, 0
    for j in range(9):
        y, k = map(int, input().split())
        y_score += y
        k_score += k
    
    if y_score > k_score:
        print("Yonsei")
    elif y_score < k_score:
        print("Korea")
    else:
        print("Draw")
    
