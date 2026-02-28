def solution(n, s, a, b, fares):
    adj_matrix = [[999999 for _ in range(n)] for _ in range(n)]
    start_point = s-1
    a_house = a-1
    b_house = b-1
    for i in range(len(adj_matrix)):
        adj_matrix[i][i] = 0
    
    for fare in fares:
        fr, to, cost = fare
        adj_matrix[fr-1][to-1] = cost
        adj_matrix[to-1][fr-1] = cost
    
    for hub in range(n):
        for fr in range(n):
            for to in range(n):
                adj_matrix[fr][to] = min(adj_matrix[fr][to], adj_matrix[fr][hub] + adj_matrix[hub][to])
    min_cost = 99999999  
    # straight 
    for hub_index in range(n):
        start_to_hub = adj_matrix[start_point][hub_index]
        hub_to_a = adj_matrix[hub_index][a_house]
        hub_to_b = adj_matrix[hub_index][b_house]
        min_cost = min(hub_to_a + hub_to_b + start_to_hub, min_cost)

    return min_cost