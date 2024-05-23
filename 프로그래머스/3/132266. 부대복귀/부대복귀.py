from collections import deque, defaultdict
def solution(n, roads, sources, destination):
    answer = []
    que = deque()
    adj = defaultdict(list)
    for i in roads:
        fr,to = i
        adj[fr].append(to)
        adj[to].append(fr)
    que.append((0,destination))
    visited = {}
    visited[destination] = 0
    while que:
        count, road = que.popleft()
        for i in adj[road]:
            if i not in visited:
                visited[i] = count+1
                que.append((count+1,i))
    for i in sources:
        if i not in visited:
            answer.append(-1)
        else:
            answer.append(visited[i])
    return answer