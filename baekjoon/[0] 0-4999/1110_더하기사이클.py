N = int(input())

cnt, n = 0, N
while True:
    cnt += 1
    ten, one = n//10, n%10
    new_one, new_ten = ( ten + one ) % 10, one
    result = new_ten*10 + new_one
    
    if result == N:
        break
    else:
        n = result

print(cnt)
