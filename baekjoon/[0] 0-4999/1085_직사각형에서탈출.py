x, y, w, h = map(int, input().split())

diff_list = [w-x, h-y, x, y]

print(min(diff_list))
