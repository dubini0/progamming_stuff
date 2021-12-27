hour, minute = input().split(' ')
hour, minute = int(hour), int(minute)

if minute >= 45:
    print(f"{hour} {minute - 45}")
else:
    if hour == 0:
        print(f"23 {15 + minute}")
    else:
        print(f"{hour-1} {15 + minute}")
