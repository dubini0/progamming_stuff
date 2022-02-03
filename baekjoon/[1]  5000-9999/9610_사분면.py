n = int(input())

points = []
for i in range(n):
    a, b = map(int, input().split())
    points.append([a, b])

quadrant = [0, 0, 0, 0, 0]
for x, y in points:
    if x > 0:
        if y > 0:
            quadrant[1] += 1
        elif y < 0:
            quadrant[4] += 1
        else:
            quadrant[0] += 1
    elif x < 0:
        if y > 0:
            quadrant[2] += 1
        elif y < 0:
            quadrant[3] += 1
        else:
            quadrant[0] += 1
    else:
        quadrant[0] += 1

for i in range(4):
    print(f"Q{i+1}: {quadrant[i+1]}")
print(f"AXIS: {quadrant[0]}")
