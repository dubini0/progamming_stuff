t = int(input())
for i in range(t):
    n, ref_str = map(str, input().split())
    for j in ref_str:
        print(j*int(n), end="")
    print()
