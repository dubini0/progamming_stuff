n = int(input())

for i in range(n):
    eq = list(map(str, input().split()))
    answer = float(eq[0])
    for i in range(1, len(eq)):
        if eq[i] == "#":
            answer -= 7
        elif eq[i] == "%":
            answer += 5
        elif eq[i] == "@":
            answer *= 3

    print("%0.2f"%answer)
