# BFS 형태로 업데이트 하면서 푸는 문제
from collections import deque

def find_first(maps):
    one_list = []
    for zidx, cin in enumerate(maps):
        for cidx, rin in enumerate(cin):
            for ridx, zin in enumerate(rin):
                if zin == 1:
                    one_list.append((zidx, cidx, ridx, 1))
    return one_list

num_col, num_row, num_h = map(int, input().split())
maps = []
for i in range(num_h):
    maps_2_input = []
    for j in range(num_row):
        maps_2_input.append(list(map(int, input().split())))
    maps.append(maps_2_input)

queue = find_first(maps)
queue = deque(queue)
answer = 0

while queue:
    #print(queue)
    next_z, next_y, next_x, time_cost = queue.popleft()
    dx = [0, 0, -1, 1, 0, 0]
    dy = [-1, 1, 0, 0, 0 ,0]
    dz = [0, 0, 0, 0, -1, 1]
    #print(next_z, next_y, next_x)
    for chidx in range(len(dx)):
        tdx = dx[chidx]
        tdy = dy[chidx]
        tdz = dz[chidx]
        candid_z, candid_y, candid_x = next_z + tdz, next_y + tdy, next_x + tdx
        #print(candid_y, candid_x)
        if candid_y > -1 and candid_y < len(maps[0]):
            if candid_x > -1 and candid_x < len(maps[0][0]):
                if candid_z > -1 and candid_z < len(maps):
                    if maps[candid_z][candid_y][candid_x] == 0:
                        maps[candid_z][candid_y][candid_x] = 1
                        queue.append((candid_z, candid_y, candid_x, time_cost+1))
                        answer = max(time_cost, answer)
solved = True
for i in maps:
    for j in i:
        for k in j:
            if k == 0:
                solved = False
if solved:
    print(answer)
else:
    print(-1)

