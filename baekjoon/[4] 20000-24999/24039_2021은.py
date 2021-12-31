prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
n = int(input())

for i in range(len(prime_list)-1):
    try_number = prime_list[i]*prime_list[i+1]
    if try_number > n:
        print(try_number)
        break
