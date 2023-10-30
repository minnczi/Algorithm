# 이진탐색트리 - 생성
"""
1. 루트부터 트리를 탐색한다
2. 현재 노드보다 작으면 왼쪽, 크면 오른쪽으로 보낸다
3. 더이상 비교할 자식 노드가 없으면 부모 노드의 인덱스를 해당 노드의 자리에 저장한다
"""

def add_node(node, num):
    if not tree[node]:
        tree[nums[num]]


N = int(input())
nums = list(map(int, input().split()))
tree = [0] * (N+1)
tree[1] = nums[0]


