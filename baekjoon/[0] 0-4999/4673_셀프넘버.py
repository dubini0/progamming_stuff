# Note : This only works with Pypy3.
# Python gets a timeout
def is_self_num(n):
    for i in range(n):
        res = i
        for j in str(i):
            res += int(j)
        if res == n:
            return
    print(n)
    return

if __name__ == "__main__":
    for i in range(10000):
        is_self_num(i+1)
