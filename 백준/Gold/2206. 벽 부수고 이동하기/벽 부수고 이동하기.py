import copy
from collections import deque

def bfs(maps):
    queue = deque([(0, 0, 1, True)])
    visited = [[],[]]
    for i in maps:
        temp_visited = []
        for j in i:
            if j == 1:
                temp_visited.append(-1)
            else:
                temp_visited.append(0)
        visited[0].append(temp_visited)
        visited[1].append(copy.deepcopy(temp_visited))

    reach_goal = []
    while queue:
        next_target_y, next_target_x, cost, can_pass = queue.popleft()
        for dy, dx in zip([0,0,-1,1],[-1,1,0,0]):
            candidate_y, candidate_x, candidate_cost, candid_can_pass = next_target_y + dy, next_target_x + dx, cost + 1, can_pass
            if 0 <= candidate_y <= len(maps) -1 and 0 <= candidate_x <= len(maps[0])-1:
                if candidate_y == len(maps)-1 and candidate_x == len(maps[0])-1:
                    return candidate_cost
                if can_pass == True:
                    if visited[0][candidate_y][candidate_x] == 0:
                        visited[0][candidate_y][candidate_x] = 1
                        queue.append((candidate_y, candidate_x, candidate_cost, candid_can_pass))
                    if visited[0][candidate_y][candidate_x] == -1 and candid_can_pass:
                        queue.append((candidate_y, candidate_x, candidate_cost, False))
                        visited[1][candidate_y][candidate_x] = 1
                elif can_pass == False:
                    if visited[1][candidate_y][candidate_x] == 0:
                        visited[1][candidate_y][candidate_x] = 1
                        queue.append((candidate_y, candidate_x, candidate_cost, candid_can_pass))
                    
    if len(reach_goal) == 0:
        return -1
    else:
        return min(reach_goal)

y_len, x_len = map(int, input().split())

maps_original = []
for i in range(y_len):
    maps_original.append(list(map(int, [i for i in input()])))

if y_len == 1 and x_len == 1:
    print(1)
else:
    print(bfs(maps_original))