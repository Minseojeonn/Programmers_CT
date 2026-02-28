# 맵이 주어지고, 클러스터 개수 구하는듯? 0은 배추고 1은 땅임. 
# 전형적인 BFS 문제로 보임 .
from collections import deque
num_test_case = int(input())
for _ in range(num_test_case):
    x_len, y_len, num_baechu = map(int, input().split())
    visited = [[1 for _ in range(x_len)] for _ in range(y_len)]
    for _ in range(num_baechu):
        x_pos, y_pos = map(int, input().split(" "))
        visited[y_pos][x_pos] = 0
    
    num_cluster = 0
    for i in range(y_len):
        for j in range(x_len):
            cur_pos_y, cur_pos_x = i, j 
            if visited[cur_pos_y][cur_pos_x] == 1:
                continue
            else:
                num_cluster+=1
                queue = deque([(cur_pos_y, cur_pos_x)])
                visited[cur_pos_y][cur_pos_x] = 1
                while queue:
                    next_pos_y, next_pos_x = queue.popleft()
                    for dy, dx in zip([0, 0, -1, +1], [-1, +1, 0, 0]):
                        candid_pos_y, candid_pos_x = next_pos_y+dy, next_pos_x+dx
                        if 0 <= candid_pos_y <= y_len-1 and 0 <= candid_pos_x <= x_len-1:
                            if visited[candid_pos_y][candid_pos_x] == 0:
                                visited[candid_pos_y][candid_pos_x] = 1
                                queue.append((candid_pos_y, candid_pos_x))
    
    print(num_cluster)
        
        
