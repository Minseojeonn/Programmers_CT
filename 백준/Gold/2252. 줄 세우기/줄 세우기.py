from collections import deque
num_students, num_edges = map(int, input().split())
adj_list = [[] for _ in range(num_students+1)]
in_degree = [0 for _ in range(num_students+1)]

for _ in range(num_edges):
    a, b = map(int, input().split(" "))
    adj_list[a].append(b)
    in_degree[b] += 1
    
queue = deque([i for i in range(1, num_students+1) if in_degree[i] == 0])
result = []
while queue:
    curr = queue.popleft()
    result.append(curr)
    
    for next_node in adj_list[curr]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            queue.append(next_node)

print(*(result))
