alphabet = [char for char in "abcdefghijklmnopqrstuvwxyz"]
alpha_len = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

a = input().lower()
b = input().lower()

target = []
for i in range(len(a)):
    target.append(alpha_len[alphabet.index(a[i])])
    target.append(alpha_len[alphabet.index(b[i])])

while len(target) != 2:
    for i in range(len(target)-1):
        target[i] = (target[i] + target[i+1]) % 10
    del target[-1]
    #print(target)

print("".join(map(str, target)))
