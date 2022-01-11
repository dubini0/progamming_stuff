vowel = "aeiou"

string = input()
cnt = 0
for i in string:
    if i in vowel:
        cnt += 1

print(cnt)
