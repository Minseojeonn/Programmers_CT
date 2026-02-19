from collections import deque
#y 축 reverse 문제
def y_converter(ypos, ylen):
    ypos_return = ylen-ypos
    return ypos_return-1

def bfs(maps, start_point):
    queue = deque([start_point])
    land_size = 1
    while queue:
        next_target = queue.popleft()
        next_y, next_x = next_target
        for dy, dx in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            candid_y, candid_x = next_y + dy, next_x + dx
            if 0 <= candid_y <= len(maps)-1 and 0 <= candid_x <= len(maps[0])-1:
                if maps[candid_y][candid_x] == 0:
                    maps[candid_y][candid_x] = 1
                    land_size += 1
                    queue.append((candid_y, candid_x))
    
    return land_size
        
ylen, xlen, num_square = map(int, input().split())

maps = []

for i in range(ylen):
    temp_list = [0 for _ in range(xlen)]
    maps.append(temp_list)
    
for i in range(num_square):
    leftdownx, leftdowny, rightupx, rightupy = map(int, input().split(" "))
    for y in range(leftdowny, rightupy):
        for x in range(leftdownx, rightupx):
            maps[y_converter(y, ylen)][x] = -1
    
answer = []
for idx, i in enumerate(maps):
    for jdx, j in enumerate(i):
        if maps[idx][jdx] == 0:
            maps[idx][jdx] = 1
            land_size_temp = bfs(maps, (idx, jdx))
            answer.append(land_size_temp)

print(len(answer))
print(" ".join(list(map(str,sorted(answer)))))
