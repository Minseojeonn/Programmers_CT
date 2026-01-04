def solution(N, road, K):
    
    edges = {}
    
    for i in range(N+1):
        edges[i] = []
    
    for roa in road:
        fr, to, cost = roa
        edges[fr].append([to, cost])
        edges[to].append([fr, cost])
        
    time_cost = [float('inf') for _ in range(N+1)]
    time_cost[1] = 0
    
    queue = [1]
    
    while queue:
        start_point = queue.pop()
        destination = edges[start_point]
        for dest in destination:
            de, co = dest
            new_cost = time_cost[start_point] + co
            if new_cost <= time_cost[de]:
                queue.append(de)
                time_cost[de] = new_cost
    
    answer = 0
    for val in time_cost:
        if val <= K:
            answer += 1
    return answer

# 1. undirect 로 모든 edge를 저장하고
# 2. 1부터 while문으로 반복종료까지 아래 시도
#업데이트가 되면, 연결된 지점들도 다 업데이트 시도하기.