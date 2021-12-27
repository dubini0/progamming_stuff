from itertools import product

def get_hash(n_list):
    hash_val = 0
    n = len(n_list)
    for i in range(n):
        hash_val += n_list[i]*(31**(n-i-1))
    return hash_val % 1000000007

def get_max_string_len(hash_val):
    for string_len in range(30):
        min_val = sum([31**i for i in range(string_len+1)])
        if min_val > hash_val:
            return string_len

def get_hash_crash(hash_val):
    result = 0
    string_len = get_max_string_len(hash_val)
    #print(string_len)
    for j in range(string_len):
        n_list = [i for i in product(list(range(32, 127)), repeat=j)]
        for i in range(len(n_list)):
            hash_cal = get_hash(list(n_list[i]))
            if hash_cal == hash_val:
                result += 1

    return result

if __name__ == "__main__":
    while True:
        n_list = list(map(int, input().split()))
        if n_list == [0]:
            exit()
        del n_list[0]
        hash_val = get_hash(n_list)
        result = get_hash_crash(hash_val)
        # print(f"result : {result}")
        print(result)
