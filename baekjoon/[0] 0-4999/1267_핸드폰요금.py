n = int(input())
n_list = list(map(int, input().split()))

y_sum, m_sum = 0, 0
for i in n_list:
    y_sum += (i // 30 + 1)*10
    m_sum += (i // 60 + 1)*15

if y_sum == 0:
    y_sum = 10
elif m_sum == 0:
    m_sum = 15

if m_sum > y_sum:
    print("Y", y_sum)
elif m_sum < y_sum:
    print("M", m_sum)
else:
    print("Y M", m_sum)
