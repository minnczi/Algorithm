from copy import deepcopy
def solution(info, edges):
    AL = [[] for _ in range(len(info))]
    for a, b in edges:
        AL[a].append(b)
        AL[b].append(a)
    
    stack = [[0,0,0,[0]]]
    
    answer = 0
    while stack:
        node, S, W, visited = stack.pop(0)
        
        if info[node]:
            W += 1
        else:
            S += 1
        
        if W >= S:
            continue
        answer = max(answer, S)
        
        for n in visited:
            for sheep in AL[n]:
                if sheep not in visited:
                    visited_copy = deepcopy(visited)
                    visited_copy.append(sheep)
                    stack.append([sheep, S, W, visited_copy])

    return answer