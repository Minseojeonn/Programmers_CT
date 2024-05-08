from collections import deque
def solution(n, computers):
    answer = 0
    #computers is adj matrix
    visited = [0 for i in range(n)]
    for idx in range(n):
        if visited[idx] == 1:
            continue
        else:
            answer += 1
            que = deque()
            que.append(idx)
            visited[idx] = 1
            while que:
                now = que.popleft()
                for idx, i in enumerate(computers[now]):
                    if i == 1 and visited[idx] == 0:
                        visited[idx] = 1
                        que.append(idx)
    
    return answer