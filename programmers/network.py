def connection(idx, n, computers, connection_list):
    for j in range(idx, n):
        if j not in connection_list:
            print(j)
            pass
        elif computers[idx][j] == 1:
            print(idx, j)
            connection_list.pop(connection_list.index(idx))
            idx = j
            print(idx)
            return connection(idx, n, computers, connection_list)


def solution(n, computers):
    answer = 0
    connection_list = list(range(0, n))
    for i in range(0, n):
        computers[i][i] = 0

    connection(0, n, computers, connection_list)
    answer = len(connection_list)
    return answer
