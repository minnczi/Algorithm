import sys
sys.stdin = open('1289_input.txt', 'r')

def change_count(bit):
    start = bit.find('1')
    # print("start", start)
    # 만약 target이 00000000 일 경우
    if start == -1:
        return 0
    
    cnt = 1
    now = '1'
    # 0 <-> 1 로 바뀔때마다 수정 횟수가 1회 늘어남
    for i in range(start+1, len(bit)):
        if bit[i] != now:
            now = bit[i]
            cnt += 1
    return cnt

# 출력
T = int(input())
for tc in range(1, T+1):
    cnt = change_count(input())
    print('#%d %d' % (tc, cnt))