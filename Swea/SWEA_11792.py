import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, hexa = input().split()
    print("#%d %s" % (tc, bin(int(hexa, 16))[2:].zfill(len(hexa)*4)))

