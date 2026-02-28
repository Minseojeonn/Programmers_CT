# 격자판 주어짐
# 연속된 MOBIS 단어 찾기 
# DFS 인데, 조건분기 하는것 같음. 일단 DFS 풀어볼듯 - 연속임.
# 격자판 크기는 100 바이 100 이하인듯.
from collections import deque

matrix_size = int(input())
matrix = []
for _ in range(matrix_size):
    matrix.append(list(input()))

target_str = ["M","O","B","I","S"]
num_string = 0
dy, dx = [0, 0, -1, +1, -1, -1, +1, +1], [-1, +1, 0, 0, -1, +1, -1, +1]
for ypos, row in enumerate(matrix):
    for xpos, col_str in enumerate(row):
        if col_str == target_str[0]:
            queue = deque([])        
            for direction in range(len(dy)):
                queue.append((0, ypos, xpos, direction))
            while queue:
                cur_depth, cur_y, cur_x, direction = queue.popleft() #대각선
                next_y, next_x = cur_y + dy[direction], cur_x + dx[direction]
                if 0 <= next_y <= matrix_size-1 and 0 <= next_x <= matrix_size-1:
                    if matrix[next_y][next_x] == target_str[cur_depth+1]:
                        if cur_depth+1 == 4:
                            num_string+=1
                        else:
                            queue.append((cur_depth+1, next_y, next_x, direction))
                        
                    
                    
print(num_string)    