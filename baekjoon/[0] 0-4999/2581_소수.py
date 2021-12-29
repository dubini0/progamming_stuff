def is_prime(n):
    if n<2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a = int(input())
b = int(input())

prime_list = []
for i in range(a, b+1):
    if is_prime(i):
        prime_list.append(i)

if prime_list == []:
    print(-1)        
else:
    print(sum(prime_list))
    print(prime_list[0])
