num_nodes = int(input())
num_edge = int(input())
edge_dict = {}

for i in range(num_nodes+1):
    edge_dict[i] = []

node_adj = [[float("INF") for _ in range(num_nodes+1)] for _ in range(num_nodes+1)]

for edge in range(num_edge):
    fr, to, edge_cost = map(int, input().split(" "))
    node_adj[fr][to] = min(node_adj[fr][to], edge_cost)

# 1. 초기 설정: 자기 자신으로 가는 비용은 0
for i in range(1, num_nodes + 1):
    node_adj[i][i] = 0

for k in range(1, num_nodes + 1):          # 경유지 (가장 바깥쪽!)
    for i in range(1, num_nodes + 1):      # 출발지
        for j in range(1, num_nodes + 1):  # 도착지
            # i에서 j로 바로 가는 것 vs i에서 k 찍고 k에서 j로 가는 것 비교
            if node_adj[i][j] > node_adj[i][k] + node_adj[k][j]:
                node_adj[i][j] = node_adj[i][k] + node_adj[k][j]

for i in node_adj[1:]:
    temp_list = []
    for j in i[1:]:
        if j == float("inf"):
            temp_list.append("0")
        else:
            temp_list.append(str(j))
    print(" ".join(temp_list))

