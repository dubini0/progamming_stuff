a, b = map(int, input().split())
c, d = map(int, input().split())

tmp1 = a/c + b/d
tmp2 = c/d + a/b
tmp3 = d/b + c/a
tmp4 = b/a + d/c

result = [tmp1, tmp2, tmp3, tmp4]
max_val = max(result)
print(result.index(max_val))
