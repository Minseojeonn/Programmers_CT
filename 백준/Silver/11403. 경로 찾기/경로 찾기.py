import sys

num_nodes = int(sys.stdin.readline().strip())

adj_dict = dict()
for idx in range(num_nodes):
    adj_dict[idx] = []
result_matrix = []

for idx in range(num_nodes):
    for jdx, edge in enumerate(list(map(int, sys.stdin.readline().strip().split()))):
        if edge == 1:
            adj_dict[idx].append(jdx)

for source_node in adj_dict:
    temp_row = [0] * num_nodes
    queue = [source_node]
    visited = {}
    while queue:
        next = queue.pop(0)
        for candidate in adj_dict[next]:
            if candidate in visited:
                continue
            visited[candidate] = True
            temp_row[candidate] = 1
            queue.append(candidate)
    result_matrix.append(temp_row)
        

for i in range(len(result_matrix)):
    print(' '.join(map(str, result_matrix[i])))

    

