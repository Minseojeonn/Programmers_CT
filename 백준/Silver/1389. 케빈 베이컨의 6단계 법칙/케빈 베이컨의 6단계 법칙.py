num_node, num_edge = map(int,input().split(" "))
adj_matrix = [[9999999 for _ in range(num_node)] for _ in range(num_node)]

for _ in range(num_edge):
    fr, to = map(int, input().split(" "))
    adj_matrix[fr-1][to-1] = 1
    adj_matrix[to-1][fr-1] = 1

for i in range(num_node):
    adj_matrix[i][i] = 0


for i in range(num_node): #hub
    for j in range(num_node): #from
        for k in range(num_node): #to
            adj_matrix[j][k] = min(adj_matrix[j][i] + adj_matrix[i][k], adj_matrix[j][k]) 

min_value, min_idx = 999999, -1
for idx, value in enumerate(adj_matrix):
    if sum(value) < min_value:
        min_value = sum(value)
        min_idx = idx+1

print(min_idx)