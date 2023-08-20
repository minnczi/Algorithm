import sys

sys.stdin = open("sample_input_bus.txt", "r")

T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split())
    gas_station = list(map(int, input().split()))
    all_stations = [0] * (N + 1)

    # 충전소가 설치된 정류장은 1로 표시
    for i in gas_station:
        all_stations[i] = 1

    # 버스의 현재위치
    now = 0
    fuel = 0

    while now < (N-K) and fuel >= 0:
        for station_num in range(now+K, now, -1):
            if all_stations[station_num] == 1:
                now = station_num
                fuel += 1
                break
        else:
            fuel = -1
            break

    if fuel == -1:
        print('#%d 0' % t)
    else:
        print('#%d %d' % (t, fuel))

