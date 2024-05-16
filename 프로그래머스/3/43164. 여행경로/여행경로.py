from collections import deque
import copy
def solution(tickets):
    answer = []
    edge = {}
    end = len(tickets)+1
    for i in tickets:
        fr, to = i
        if fr in edge:
            edge[fr].append(to)
        else:
            edge[fr] = [to]
    for i in edge:
        edge[i] = sorted(edge[i])
    target = (["ICN"],copy.deepcopy(edge))
    dp = deque([target])
    while dp:
        visited, edges = dp.popleft()
        if len(visited) == end:
            answer = visited
            break
        else:
            if visited[-1] in edges:
                candidate = edges[visited[-1]]
                for idx,land in enumerate(candidate):
                    t_visited = copy.deepcopy(visited)
                    t_edge = copy.deepcopy(edges)
                    del t_edge[visited[-1]][idx]
                    t_visited.append(land)
                    dp.append((t_visited,t_edge))
            
        
    
    
    return answer