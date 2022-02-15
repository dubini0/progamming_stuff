import string

lc = string.ascii_lowercase
uc = string.ascii_uppercase
trans = str.maketrans(lc + uc, lc[13:] + lc[:13] + uc[13:] + uc[:13])
rot13 = lambda s: str.translate(s, trans)

input_str = input()
print(rot13(input_str))
