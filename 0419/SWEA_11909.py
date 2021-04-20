# SWEA 11909 트리 순회
# 전위순회
def preorder(n):
    if n>0:
        print(n, end='-')
        preorder(left[n])
        preorder(right[n])

# 중위순회
def midorder(n):
    if n>0:
        midorder(left[n])
        print(n, end=' ')
        midorder(right[n])

# 후위순회
def postorder(n):
    if n>0:
        postorder(left[n])
        postorder(right[n])
        print(n, end=' ')

V = int(input())
edges = list(map(int, input().split()))

# 부모 인덱스에 자식의 번호 저장
left = [0]*(V+1)
right = [0]*(V+1)

for i in range(V-1):
    n1, n2 = edges[i*2], edges[i*2+1]
    # 이미 왼쪽 자식이 있으면 오른쪽에 저장
    if left[n1]:
        right[n1] = n2
    # 아니라면 왼쪽에 저장
    else:
        left[n1] = n2


