N = int(input())

for i in range(N):
    n_list = list(map(int, input().split()))
    del n_list[0]
    sum = 0
    for i in range(len(n_list)):
        sum += n_list[i]
    avg = sum / len(n_list)
    
    student_cnt = [i for i in n_list if i > avg]
    print("{:.3f}%".format(len(student_cnt)/len(n_list)*100))
