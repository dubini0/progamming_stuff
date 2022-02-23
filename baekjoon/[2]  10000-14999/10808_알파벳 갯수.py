str_input = input()

letter_count = dict([(chr(i),0) for i in range(97,123)])
for s in str_input:
    letter_count[s] += 1

for k, v in letter_count.items():
    print(v, end=' ')
