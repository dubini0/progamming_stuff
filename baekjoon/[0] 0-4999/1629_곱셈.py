def divideAndConquer(a, b, c):
    if b == 1:
        return a % c
    tmp = divideAndConquer(a, b//2, c)
    if b % 2 == 0:
        return (tmp**2) % c
    else:
        return (tmp**2*a)%c

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(divideAndConquer(a, b, c))
