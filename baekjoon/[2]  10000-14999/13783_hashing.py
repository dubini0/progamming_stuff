# NOT DONE YET!
# WORKING ON IT, HAVING MEMEORY ISSUES

from itertools import product

def get_hash(n_list):
    hash_val = 0
    n = len(n_list)
    for i in range(n):
        hash_val += n_list[i]*(31**(n-i-1))
    return hash_val % 1000000007

def get_hash_crash(hash_val):
    string_len, result = 1, 0
    while True:
        min_val = sum([31**i for i in range(string_len)])
        if min_val > hash_val:
            return result
        n_list = [i for i in product(list(range(32, 127)), repeat=string_len)]
        for i in range(len(n_list)):
            hash_cal = get_hash(list(n_list[i]))
            if hash_cal == hash_val:
                result += 1
        string_len += 1

if __name__ == "__main__":
    while True:
        n_list = list(map(int, input().split()))
        if n_list == [0]:
            exit()
        del n_list[0]
        hash_val = get_hash(n_list)
        result = get_hash_crash(hash_val)
        #print(hash_val)
        print(result)
