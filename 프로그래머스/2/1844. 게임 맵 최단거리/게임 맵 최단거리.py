from collections import deque
from copy import deepcopy
def solution(maps):
    answer = 0
    queue = deque()
    
    dcol = [0, 0, +1 , -1]
    drow = [-1, +1, 0, 0]
    
    visited = deepcopy(maps)
    visited_tiles = 0
    for row in maps:
        for col in row:
            if col == 0:
                visited_tiles += 1
    visited_tiles += 1
    queue.append((0,0,1))
    
    while queue:
        cur_position_col, cur_position_row, cur_cost = queue.popleft()
        for idx in range(4):
            next_position_col = cur_position_col + dcol[idx]
            next_position_row = cur_position_row + drow[idx]
            
            if next_position_col > -1 and next_position_col < len(visited) and next_position_row > -1 and next_position_row < len(visited[0]) :
                    if visited[next_position_col][next_position_row] == 1:
                        queue.append((next_position_col, next_position_row, cur_cost+1))
                        visited[next_position_col][next_position_row] = 0
                    if next_position_col == len(visited)-1 and next_position_row == len(visited[0])-1: 
                        return cur_cost+1
    
    return -1
            
    
    
 