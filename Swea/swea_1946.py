import sys
sys.stdin = open('1946_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    string = ''
    for _ in range(int(input())):
        letter, rep = map(str, input().split())
        string += letter * int(rep)

    print('#%d' % tc)
    for i in range(0, len(string), 10):
        print(string[i:i+10])

