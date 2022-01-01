l, p = map(int, input().split())
n_list = list(map(int, input().split()))

for i in n_list:
    print(i - l*p, end=' ')
