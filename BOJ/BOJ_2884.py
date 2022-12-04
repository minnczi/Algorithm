H, M = map(int, input().split())

minutes = H * 60 + M
alarm_minutes = minutes - 45

if alarm_minutes < 0:
    print("23", 60 + alarm_minutes)
else:
    print(alarm_minutes // 60, alarm_minutes % 60)