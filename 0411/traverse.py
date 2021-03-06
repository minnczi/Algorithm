import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())
edges = list(map(int, input().split()))

# 부모 인덱스에 자식의 번호 저장
left = [0]*(V+1)
right = [0]*(V+1)

for i in range(E):
    n1, n2 = edges[i*2], edges[i*2+1]
    # 이미 왼쪽 자식이 있으면 오른쪽에 저장
    if left[n1]:
        right[n1] = n2
    # 아니라면 왼쪽에 저장
    else:
        left[n1] = n2

print(left, right)

# 자식을 인덱스로 부모의 번호 저장
pa = [0]*(V+1)
for i in range(E):
    n1, n2 = edges[i*2], edges[i*2+1]
    pa[n2] = n1
print(pa)

# 루트를 찾는 코드
root = 0
# 부모가 없으면 루트이다
for i in range(1, V+1):
    if pa[i] == 0:
        root = i
        break
print(root)

# 전위순회
def preorder(n):
    if n>0:
        print(n, end=' ')
        preorder(left[n])
        preorder(right[n])

preorder(2)
print("")
# 중위순회
def midorder(n):
    if n>0:
        midorder(left[n])
        print(n, end=' ')
        midorder(right[n])

midorder(2)
print("")

# 후위순회
def postorder(n):
    if n>0:
        postorder(left[n])
        postorder(right[n])
        print(n, end=' ')

postorder(2)