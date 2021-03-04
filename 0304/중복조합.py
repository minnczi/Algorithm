a = ['배', '감', '귤']
n, k = 3, 3

# for문으로 짜는 방법
def rep_combo(a, n):
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                print(a[i], a[j], a[k])

# rep_combo(a, k)

arr = [''] * n
# 재귀로 짜는 방법
def rep_combo_recursive(level, start):
    if level == k:
        print(arr)
        return
    for i in range(start, n):
        arr[level] = a[i]
        rep_combo_recursive(level+1, i)

rep_combo_recursive(0, 0)
