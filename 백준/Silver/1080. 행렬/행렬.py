len_y, len_x = map(int, input().split())

matrix_A = []
matrix_B = []

for i in range(2):
    if i == 0:
        for _ in range(len_y):
            matrix_A.append(list(map(int, input())))
    elif i == 1:
        for _ in range(len_y):
            matrix_B.append(list(map(int, input())))

num_change = 0
for y_pos in range(len_y):
    for x_pos in range(len_x):
        if matrix_A[y_pos][x_pos] != matrix_B[y_pos][x_pos]:
            num_change += 1
            if y_pos < len_y-2 and x_pos < len_x-2 :
                for i in range(3):
                    for j in range(3):
                        if matrix_A[y_pos+i][x_pos+j] == 0:
                            matrix_A[y_pos+i][x_pos+j] = 1
                        else:
                            matrix_A[y_pos+i][x_pos+j] = 0

if matrix_A == matrix_B:
    print(num_change)
else:
    print(-1)