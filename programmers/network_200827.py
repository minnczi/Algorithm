#####################################################
# 문제 설명
# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다.
# 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때
# 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다.
# 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
#
# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때,
# 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
#
# 제한사항
# 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# computer[i][i]는 항상 1입니다.
# visited_list = []
# answer = 0
#####################################################

def find_one_connection(n, computers, n_start_queue):
    global answer
    queue = [n_start_queue]
    while queue:
        current = queue.pop(0)
        visited_list.append(current)
        for j in range(0, n):
            if computers[current][j] == 1 and j not in (queue + visited_list):
                queue.append(j)
    answer += 1


def solution(n, computers):
    for i in range(0, n):
        if i not in visited_list:
            find_one_connection(n, computers, i)
        else:
            pass
    return answer


# def connection(idx, n, computers, connection_list):
#     for j in range(idx,n):
#         if j not in connection_list:
#             print(j)
#             pass
#         elif computers[idx][j] == 1:
#             print(idx, j)
#             connection_list.pop(connection_list.index(idx))
#             idx = j
#             print(idx)
#             return connection(idx, n, computers, connection_list)

# Attempt #2
# visited_list = []
# answer = 0

# def find_one_connection(n, computers, idx):
#     global answer
#     visited_list.append(idx)
#     if idx+1 == n:
#         answer += 1
#     else:
#         for j in range(idx+1,n):
#             if computers[idx][j]==1:
#                 idx = j
#                 return find_one_connection(n,computers,idx)
#             else:
#                 answer += 1

# def solution(n, computers):
#     global answer
#     for idx in range(0,n):
#         if idx in visited_list:
#             pass
#         else:
#             find_one_connection(n, computers, idx)
#     return answer


# Attempt 3