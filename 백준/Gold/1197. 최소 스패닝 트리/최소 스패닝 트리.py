import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
num_node, num_edge = map(int, input().split(" "))

edge_list = []
parent = [i for i in range(num_node)]

def find_root(fr):
    if parent[fr] == fr: #root_node
        return fr
    else:
        parent[fr] = find_root(parent[fr])
        return parent[fr]

for i in range(num_edge):
    fr, to, cost = map(int, input().split(" "))
    edge_list.append((cost, fr-1, to-1))

sum_cost = 0
edge_list.sort()

for edge in edge_list:
    cost, fr, to = edge
    root_fr = find_root(fr)
    root_to = find_root(to)
    if root_fr != root_to:
        sum_cost+=cost
        parent[root_to] = root_fr
    
print(sum_cost)