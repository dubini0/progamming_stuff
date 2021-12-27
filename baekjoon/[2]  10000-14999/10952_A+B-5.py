while True:
    a, b = input().split()
    a, b = int(a), int(b)

    if a == 0 and b == 0:
        exit()
    else:
        print(a+b)
