# 15683 beakjoon
import copy
ylen, xlen = map(int, input().split(" "))
maps = []
init_visited = []
camera_position = []
global answer 
answer = float("inf")

def draw_view(camera, direction, visited):
    ypos, xpos, c_type = camera
    c_direction = direction
    
    if c_type == 5:
        dx, dy = [-1, +1, 0, 0], [0, 0, -1, +1]
    if c_type == 4:
        if c_direction == 0:
            dx, dy = [-1, +1, 0], [0, 0, -1]
        if c_direction == 1:
            dx, dy = [0, +1, 0], [+1, 0, -1]
        if c_direction == 2:
            dx, dy = [0, -1, 0], [+1, 0, -1]
        if c_direction == 3:
            dx, dy = [-1, +1, 0], [0, 0, +1]
    if c_type == 3:
        if c_direction == 0:
            dx, dy = [+1, 0], [0, -1]
        if c_direction == 1:
            dx, dy = [+1, 0], [0, +1]
        if c_direction == 2:
            dx, dy = [-1, 0], [0, -1]
        if c_direction == 3:
            dx, dy = [-1, 0], [0, +1]
    if c_type == 2:
        if c_direction == 0:
            dx, dy = [-1, +1], [0, 0]
        if c_direction == 1:
            dx, dy = [0, 0], [-1, +1]
        if c_direction == 2:
            dx, dy = [-1, +1], [0, 0]
        if c_direction == 3:
            dx, dy = [0, 0], [-1, +1]
    if c_type == 1:
        if c_direction == 0:
            dx, dy = [0], [-1]
        if c_direction == 1:
            dx, dy = [0], [1]
        if c_direction == 2:
            dx, dy = [-1], [0]
        if c_direction == 3:
            dx, dy = [1], [0]
            
    for i in range(len(dx)):
        tdx, tdy = dx[i], dy[i]
        cur_y, cur_x = ypos, xpos
        visited[cur_y][cur_x] = 1
        while True:
            next_y, next_x = cur_y+tdy, cur_x+tdx
            if 0 <= next_y <= len(visited)-1 and 0 <= next_x <= len(visited[0])-1 :
                if visited[next_y][next_x] != -1:
                    visited[next_y][next_x] = 1
                    cur_y, cur_x = next_y, next_x
                else:
                    break
            else:
                break
    return

def backtrack(visited, depth):
    global answer
    if depth == len(camera_position):
        space = 0
        for i in visited:
            for j in i:
                if j == 0:
                    space += 1
        #print(visited)
        answer = min(space, answer)
    else:
        if camera_position[depth][-1] == 5:
            new_visited = copy.deepcopy(visited)
            draw_view(camera_position[depth], 0, new_visited)
            backtrack(new_visited, depth+1)
        else:
            for i in range(4):
                new_visited = copy.deepcopy(visited)
                draw_view(camera_position[depth], i, new_visited)
                backtrack(new_visited, depth+1)
            
for yidx in range(ylen):
    maps.append(list(map(int, input().split(" "))))
    temp_visited = []
    for xidx, i in enumerate(maps[-1]):
        if i != 0 and i != 6:
            camera_position.append((yidx, xidx, i))
        if i == 6:
            temp_visited.append(-1)
        else:
            temp_visited.append(0)
    init_visited.append(temp_visited)

backtrack(init_visited, 0)
print(answer)
