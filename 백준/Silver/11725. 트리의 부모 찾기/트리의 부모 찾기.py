from collections import deque
num_nodes = int(input())

adj = [[] for i in range(num_nodes+1)]
root = [-1 for i in range(num_nodes+1)]
visited = [0 for i in range(num_nodes+1)]
for i in range(num_nodes-1):
    fr, to = map(int, input().split(" "))
    adj[fr].append(to)
    adj[to].append(fr)


queue = deque([1])
visited[1] = 1
while queue:
    next_node = queue.popleft()
    for cand_node in adj[next_node]:
        if visited[cand_node] == 0:
            root[cand_node] = next_node
            queue.append(cand_node)
            visited[cand_node] = 1
for i in root[2:]:
    print(i)