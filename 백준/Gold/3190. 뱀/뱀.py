from collections import deque
len_maps = int(input())
maps = []
for i in range(len_maps):
    maps.append([0 for _ in range(len_maps)])
for i in range(int(input())):
    loc_y, loc_x = map(int, input().split())
    maps[loc_y-1][loc_x-1] = 1

snake_moves = deque([])
for i in range(int(input())):
    time_spent, direction = input().split()
    time_spent = int(time_spent)
    snake_moves.append((time_spent, direction))

direction = {
    0 : (-1, 0), #상
    1 : (0, 1), #우
    2 : (1, 0), #하
    3 : (0, -1), #좌
}

cur_location = (0,0,1) #ypos, xpos, direct
time_checker = 1
snake_body = deque([(0,0)])
while True:
    #먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    dy, dx = direction[cur_location[2]]
    next_y, next_x, next_direc = cur_location[0]+dy, cur_location[1]+dx, cur_location[2]
    
    #print(cur_location, dy, dx)
    
    if (next_y, next_x) in snake_body:
        break
    snake_body.append((next_y, next_x))
    if 0 <= next_y < len_maps and 0 <= next_x < len_maps:
        if maps[next_y][next_x] == 1:
            maps[next_y][next_x] = 0
        else:
            snake_body.popleft()
    else: #만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
       # print(f"wall at {time_checker}, ypos = {next_y}, xpos = {next_x}")
        break
    
    if snake_moves and snake_moves[0][0] == time_checker:
        target_time, direction_change = snake_moves.popleft()
        if direction_change == 'L':
            next_direc -= 1
            if next_direc == -1:
                next_direc = 3
        elif direction_change == 'D':
            next_direc += 1
            if next_direc == 4:
                next_direc = 0
    
    cur_location = (next_y, next_x, next_direc)
    
    #end 
    time_checker += 1

print(time_checker)