from itertools import combinations
import copy

def bfs(maps, walls):
    visited = copy.deepcopy(maps)
    for wall in walls:
        visited[wall[0]][wall[1]] = 1
    
    for idx, i in enumerate(visited):
        for jdx, j in enumerate(i):
            if visited[idx][jdx] == 2:
                stack = [(idx, jdx)]
                while stack:
                    now_pos_y, now_pos_x = stack.pop()
                    for dy, dx in zip([0,0,-1,1],[-1,1,0,0]):
                        candid_y = now_pos_y + dy
                        candid_x = now_pos_x + dx
                        if 0 <= candid_y < len(maps) and 0 <= candid_x < len(maps[0]):
                            if visited[candid_y][candid_x] == 0:
                                stack.append((candid_y, candid_x))
                                visited[candid_y][candid_x] = 2
    safe_zone = 0
    for i in visited:
        for j in i:
            if j == 0:
                safe_zone += 1
    
    return safe_zone
                        

y_len, x_len = map(int, input().split())
maps = []
for i in range(y_len):
    maps.append(list(map(int,input().split())))
    
#scan hole space
empty_space = []
for idx, i in enumerate(maps):
    for jdx, j in enumerate(i):
        if j == 0:
            empty_space.append((idx, jdx))

answer = 0
for walls in combinations(empty_space, 3):
    safe_zone = bfs(maps, walls)
    answer = max(safe_zone, answer)

print(answer)
