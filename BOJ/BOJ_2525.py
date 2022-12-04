hour, minute = map(int, input().split())
duration = int(input())

start_time = hour * 60 + minute
end_time = start_time + duration

end_hour, end_minute = (end_time//60) % 24, end_time % 60

print(end_hour, end_minute)
