cnt = 1
while True:
    a = int(input())
    if a == 0:
        break
    if a % 2 == 0:
        print(f"{cnt}. even {a//2}")
    else:
        print(f"{cnt}. odd {(a-1)//2}")
    cnt += 1
