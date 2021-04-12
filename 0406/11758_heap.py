import sys
sys.stdin = open('input.txt', 'r')


def heap_push(idx, child):
    if idx == 1:
        return
    
    parent = heap_tree[idx//2]
    if child < parent:
        heap_tree[idx//2], heap_tree[idx] = child, parent
        heap_push(idx//2, child)
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    heap_tree = [0]
    nums = list(map(int, input().split()))

    idx = 0
    for num in nums:
        idx += 1
        heap_tree.append(num)
        heap_push(idx, num)
    
    total = 0
    while idx > 0:
        idx //= 2
        total += heap_tree[idx]
    print("#%d %d" % (tc, total))