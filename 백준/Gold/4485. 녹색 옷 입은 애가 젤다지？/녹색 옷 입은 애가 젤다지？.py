import heapq
import copy

def cave_serach():
    maps = []
    for i in range(cave_size):
        maps.append(list(map(int, input().split(" "))))
        
    min_cost = copy.deepcopy(maps)
    for i in range(cave_size):
        for j in range(cave_size):
            min_cost[i][j] = float("INF")
            
    
    p_queue = [(maps[0][0], 0, 0)]
    while p_queue:
        #print(p_queue)
        cur_cost, cur_y, cur_x= heapq.heappop(p_queue)
        for dy, dx in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            cand_y, cand_x = cur_y + dy, cur_x + dx
            if 0 <= cand_y < len(maps) and 0 <= cand_x < len(maps[0]):
                if min_cost[cand_y][cand_x] > cur_cost + maps[cand_y][cand_x]:
                    min_cost[cand_y][cand_x] = cur_cost + maps[cand_y][cand_x]
                    heapq.heappush(p_queue, (cur_cost + maps[cand_y][cand_x], cand_y, cand_x))           
    return min_cost[-1][-1]

num_serach = 0
while True:
    num_serach += 1
    cave_size = int(input())
    if cave_size == 0:
        break
    else:
        min_cost = cave_serach()
        print(f"Problem {num_serach}: {min_cost}")
        
        
        