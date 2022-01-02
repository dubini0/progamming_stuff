for i in range(3):
    out = list(map(int, input().split()))

    count = [0, 0]
    for i in out:
        count[i] += 1

    if count[0] == 1:
        print('A')
    elif count[0] == 2:
        print('B')
    elif count[0] == 3:
        print('C')
    elif count[0] == 4:
        print('D')
    elif count[0] == 0:
        print('E')
