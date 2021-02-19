def get_MaxM(num, M):
    N = len(num)
    for i in range(M):
        for j in range(i+1, N):
            if num[j] > num[i]:
                num[j], num[i] = num[i], num[j]
    return num[0:5]