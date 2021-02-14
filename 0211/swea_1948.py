import sys
sys.stdin = open('1948_input.txt', 'r')

T = int(input())
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def num_of_days(month, day):
    days = day
    for i in range(month-1):
        days += days_in_month[i]
    return days

for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    days1 = num_of_days(m1, d1)
    days2 = num_of_days(m2, d2)

    print('#%d %d' % (tc, days2-days1+1))
