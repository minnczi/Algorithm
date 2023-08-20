# 트리의 전위순회
import sys
sys.stdin = open('tree_input.txt', 'r')

def tree(T):
    for i in AL[T]:
        result.append(str(i))
        tree(i)


N = int(input())
edges = list(map(int, input().split()))
AL = [[] for _ in range(N+1)]
result = ['1']


for i in range(0, 2*N-3, 2):
    AL[edges[i]].append(edges[i+1])

tree(1)
print("-".join(result))
