import heapq

# 1753 beakjoon
num_nodes, num_edge = map(int, input().split(" "))
start_node = int(input())

edge_dict = {}
node_cost = [float("INF") for _ in range(num_nodes+1)] #first = dummpy node

for i in range(num_nodes+1):
    edge_dict[i] = []
    
for i in range(num_edge):
    fr, to, cost = map(int,input().split(" "))
    edge_dict[fr].append((to, cost))

node_cost[start_node] = 0
queue = [(0, start_node)]

while queue:
    cur_cost, cur_node = heapq.heappop(queue)
    for edge in edge_dict[cur_node]:
        to, edge_cost = edge
        if cur_cost + edge_cost < node_cost[to]:
            node_cost[to] = cur_cost + edge_cost
            heapq.heappush(queue, (cur_cost + edge_cost, to))

for i in node_cost[1:]:
    if i == float("INF"):
        print("INF")
    else:
        print(i)