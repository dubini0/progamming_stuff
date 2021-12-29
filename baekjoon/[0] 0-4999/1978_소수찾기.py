from math import sqrt, floor

def is_prime(n):
    if n<2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())
n_list = list(map(int, input().split()))

cnt = 0
for i in n_list:
    if is_prime(i):
        cnt += 1

print(cnt)
