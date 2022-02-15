while True:
    factor = [1]
    n = int(input())
    if n == -1:
        break
    tmp = n

    # get factor
    for i in range(2, n):
        if tmp % i == 0:
            factor.append(i)
    # print(factor, sum(factor), n)

    # check if perfect
    if n == sum(factor):
        print(f"{n} =", end=" ")
        for i in factor:
            if i == factor[-1]:
                print(i)
            else:
                print(i, end=" + ")
    else:
        print(f"{n} is NOT perfect.")
