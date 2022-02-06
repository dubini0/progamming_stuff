# A: 300, B: 60, C: 10

t = int(input())

tmp = t
result = [0, 0, 0]
if tmp % 10 != 0:
    print("-1")
else:
    if tmp >= 300:
        result[0] = tmp // 300
        tmp = tmp % 300
    if tmp >= 60:
        result[1] = tmp // 60
        tmp = tmp % 60
    if tmp >= 10:
        result[2] = tmp // 10
        tmp = tmp % 10

    string_result = [str(re) for re in result]
    print(" ".join(string_result))
