num_computer = int(input())
num_edges = int(input())

edges = {}
for i in range(num_computer+1):
    edges[i] = []
for i in range(num_edges):
    fr, to = map(int, input().split())
    edges[fr].append(to)
    edges[to].append(fr)

stack = [1]
visited = [0 for _ in range(num_computer+1)]
visited[1] = 1
visited_com = 0
while stack:
    next_com = stack.pop()
    for cand_com in edges[next_com]:
        if visited[cand_com] == 0:
            visited[cand_com] = 1
            stack.append(cand_com)
            visited_com+=1
            
print(visited_com)