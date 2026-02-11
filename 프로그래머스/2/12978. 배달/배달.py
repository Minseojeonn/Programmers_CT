# num_vil = N, roads, hold=K
def solution(N, road, K):
    graph = {}
    min_cost = [9999999 for _ in range(N+1)] # 0 - no avail
    min_cost[1] = 0
    stack = []
    for ro in road:
        fr, to, val = ro
        if fr not in graph:
            graph[fr] = [(to,val)]
        else:
            graph[fr].append((to,val))
        if to not in graph:
            graph[to] = [(fr,val)]
        else:
            graph[to].append((fr,val))
    stack.append(1)
    while stack:
        cur_vil = stack.pop()
        connected_vils = graph[cur_vil]
        for connected_vil in connected_vils:
            connected_vil_num, connected_vil_cost = connected_vil
            if min_cost[cur_vil] + connected_vil_cost <= min_cost[connected_vil_num]:
                min_cost[connected_vil_num] = min_cost[cur_vil] + connected_vil_cost
                stack.append(connected_vil_num)
    answer = 0
    for i in min_cost[1:]:
        if i <= K:
            answer +=1
        

    return answer

