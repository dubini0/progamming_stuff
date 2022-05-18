import sys

n = int(sys.stdin.readline())
word_list = []

for i in range(n):
    word_list.append(sys.stdin.readline().rstrip())

word_set = list(set(word_list))
word_set.sort()
word_set.sort(key=len)

for i in word_set:
    print(i)

#print(word_sorted)
