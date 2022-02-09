N = int(input())
factor_list = list(map(int, input().split()))

max_num = max(factor_list)
min_num = min(factor_list)

print(max_num * min_num)
