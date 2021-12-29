replace_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

s = input()
for re_str in replace_list:
    s = s.replace(re_str, ".")

print(len(s))
