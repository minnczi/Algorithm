T = int(input())
for tc in range(T):
    N = int(input())
    rank = list(map(int, input().split()))
    rank_tree = [[] for _ in range(N+1)]
    rank_degree = [-1] + [0]*(N)

    # 순위상으로 하위에 있는 팀을 전부 tree에 삽입
    for i in range(N):
        rank_tree[rank[i]] = rank[i+1:]
        rank_degree[rank[i]] = i
    
    # 순위 역전 로직
    M = int(input())
    for _ in range(M):
        a,b = map(int,input().split())
        if a in rank_tree[b]:
            rank_tree[b].remove(a)
            rank_tree[a].append(b)
            rank_degree[a] -= 1
            rank_degree[b] += 1
        else:
            rank_tree[a].remove(b)
            rank_tree[b].append(a)
            rank_degree[b] -= 1
            rank_degree[a] += 1
        
    queue = []
    for i in range(1, N+1):
        if rank_degree[i] == 0:
            queue.append(i)
    if not queue:
        print('IMPOSSIBLE')
        break

    ans = []
    while queue:
        team = queue.pop(0)
        ans.append(team)
        for i in rank_tree[team]:
            rank_degree[i] -= 1
            if not rank_degree[i]:
                queue.append(i)
    if sum(rank_degree) >= 0:
        print('IMPOSSIBLE')
    else:
        print(*ans)