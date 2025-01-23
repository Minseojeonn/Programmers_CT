import sys
import itertools
from collections import deque
#init point
#state setting 
    #int = remain time
    #-1 = no bomb
    #not using 0

def print_map(matrix):
    for i in matrix:
        tp = ""
        for j in i:
            if j > 0 :
                tp += "O"
            else:
                tp += "."
        print(tp)

def search_exploded(matrix):
    target = []
    for idx, i in enumerate(matrix):
        for jdx, j in enumerate(i):
            if j == 1:
               target.append((idx, jdx)) 
    return target

def bomb_exploded(matrix):
    target = search_exploded(matrix)
    #print(target)
    for tar in target:
        row_idx, col_idx = tar
        candidate_row_idx = [row_idx, row_idx, row_idx+1, row_idx-1] 
        candidate_col_idx = [col_idx+1, col_idx-1, col_idx, col_idx]
        matrix[row_idx][col_idx] = -1
        for c_row, c_col in zip(candidate_row_idx, candidate_col_idx):
            if c_row > -1 and c_col > -1:
                if c_row < len(matrix) and c_col < len(matrix[0]):
                    matrix[c_row][c_col] = -1
    return matrix

def bomb_setting(matrix):
    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[0]):
            current_value = matrix[i][j]
            if current_value > 1:
                matrix[i][j] = current_value - 1
            if current_value == -1:
                matrix[i][j] = 2
    return matrix

row, col, tme = map(int, sys.stdin.readline().strip().split())
matrix = []
for i in range(row):
    matrix_t = []
    input_line = sys.stdin.readline().strip()
    for il in input_line:
        if il == "O":
            tt = 2
        else:
            tt = -1
        matrix_t.append(tt)
    matrix.append(matrix_t)

#solve problem
#print(f"-------------------------0-------------------------------")
#print_map(matrix)# sec 0, 1
for i in range(1,tme): #sec 2
    #print(f"-------------------------{i}-------------------------------")
    if i%2 == 1:
        matrix = bomb_setting(matrix)    
        #print(f"-------------------------bomb_setted-------------------------------")
        #print_map(matrix)
        
    else:
        matrix = bomb_exploded(matrix)
        #print(f"-------------------------bomb_exploded-------------------------------")
        #print_map(matrix)
        
print_map(matrix)
   