import heapq

def find_far(node_idx, adj_list):
    stack = []
    nodes_cost = [0 for _ in range(num_nodes+1)] #idx 0 is dummy
    visited = [0 for _ in range(num_nodes+1)] #idx 0 is dummy   
    visited[0] = 1
    visited[node_idx] = 1
    stack.append((node_idx, 0))
    while stack:
        cur_node, cur_cost = stack.pop()
        for cand_node, cand_cost in adj_list[cur_node]:
            if visited[cand_node] == 0 :
                visited[cand_node] = 1
                stack.append((cand_node, cur_cost+cand_cost))
                nodes_cost[cand_node] = cur_cost + cand_cost
    
    farest = -1
    farest_value = 0
    
    for idx, i in enumerate(nodes_cost):
        if i > farest_value:
            farest = idx
            farest_value = i
    return farest, farest_value

num_nodes = int(input())
adj_list = [[] for i in range(num_nodes+1)] # 0 is dummy

for i in range(num_nodes-1):
    fr, to, cost = map(int, input().split(" "))
    adj_list[fr].append((to, cost))
    adj_list[to].append((fr, cost))

#find farset from 1
one, cost = find_far(1, adj_list)
two, answer = find_far(one, adj_list)
print(answer)
