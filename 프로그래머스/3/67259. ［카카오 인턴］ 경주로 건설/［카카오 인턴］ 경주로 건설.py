#전부다 확인하는 대신에, 낮은숫자 나오면 갈아치우는 방식으로 진행?
from collections import deque
def solution(board):
    answer = 0
    save = [[float("inf") for i in board[0]] for j in board]
    que = deque()
    que.append((0,0,0,-1)) #y,x,sum_cost
    save[0][0] = 0
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    dir_dict = {0:1,1:1,2:0,3:0}#0 = 세로, 1 = 가로
    while que:
        y,x,sum_cost,before_dir = que.popleft()
        for i in range(4):
            next_y = y+dy[i]
            next_x = x+dx[i]
            if next_y >= 0 and next_y < len(board):
                if next_x >= 0 and next_x < len(board[0]):
                    if board[next_y][next_x] == 0:
                        if before_dir != dir_dict[i] and before_dir != -1: 
                            next_cost = sum_cost + 600
                        else:
                            next_cost = sum_cost + 100
                        if save[next_y][next_x] >= next_cost:
                            save[next_y][next_x] = next_cost
                            que.append((next_y, next_x, next_cost, dir_dict[i]))
                        elif save[next_y][next_x]+499 > next_cost:
                            que.append((next_y, next_x, next_cost, dir_dict[i]))

    
    return save[-1][-1]