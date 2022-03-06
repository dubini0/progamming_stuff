n = int(input())

for _ in range(n):
    m = int(input())
    ppl_dict = dict()
    price_list = []
    for __ in range(m):
        price, name = input().split()
        ppl_dict[int(price)] = name
        price_list.append(int(price))
    max_price = max(price_list)
    print(ppl_dict[max_price])
