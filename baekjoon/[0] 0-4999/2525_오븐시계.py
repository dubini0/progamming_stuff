hour, minute = map(int, input().split())
time = int(input())

time_hour = time // 60
time_minute = time % 60

if (minute + time_minute) >= 60:
    time_hour += (minute + time_minute) // 60
    res_minute =  (minute + time_minute) % 60
else:
    res_minute = (minute + time_minute)

if (hour + time_hour) >= 24:
    res_hour = (hour + time_hour) % 24
else:
    res_hour = (hour + time_hour)

print(res_hour, res_minute)
