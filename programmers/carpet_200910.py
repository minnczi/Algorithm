def solution(brown, yellow):
    total_tiles = brown + yellow
    for i in range (3, total_tiles//3+1):
        if total_tiles % i == 0:
            j = total_tiles / i
            i_mid = i - 2
            j_mid = j - 2
            if i_mid * j_mid == yellow:
                return [j,i]
            else:
                continue