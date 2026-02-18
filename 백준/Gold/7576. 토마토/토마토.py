# BFS 형태로 업데이트 하면서 푸는 문제
from collections import deque

def find_first(maps):
    one_list = []
    for cidx, cin in enumerate(maps):
        for ridx, rin in enumerate(cin):
            if rin == 1:
                one_list.append((cidx, ridx, 1))
    return one_list

num_col, num_row = map(int, input().split())
maps = []
for i in range(num_row):
    maps.append(list(map(int, input().split())))


queue = find_first(maps)
queue = deque(queue)

answer = 0
while queue:
    #print(queue)
    next_y, next_x, time_cost = queue.popleft()
    for dx, dy in zip([0, 0, -1, 1],[-1, 1, 0, 0]):
        candid_y, candid_x = next_y + dy, next_x + dx
        #print(candid_y, candid_x)
        if candid_y > -1 and candid_y < len(maps):
            if candid_x > -1 and candid_x < len(maps[0]):
                if maps[candid_y][candid_x] == 0:
                    maps[candid_y][candid_x] = 1
                    queue.append((candid_y, candid_x, time_cost+1))
                    answer = max(time_cost, answer)
solved = True
for i in maps:
    for j in i:
        if j == 0:
            solved = False

if solved:
    print(answer)
else:
    print(-1)
    

            