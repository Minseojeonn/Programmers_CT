def solution(key, lock):
    #shape
    key_shape = (len(key), len(key[0])) # row, col
    lock_shape = (len(lock), len(lock[0])) # row, col
    
    key_list = [key]
    for i in range(3):
        key_list.append(rotate_matrix_90_degrees(key_list[-1]))
    
    #iter - brute_force
    for y in range(-key_shape[1],lock_shape[1]): #row
        for x in range(-key_shape[0], lock_shape[0]): 
            for k in key_list:
                key_plate = [[0 for _ in lock[0]] for _ in lock]
                for y_pos, row in enumerate(k):
                    for x_pos, item in enumerate(row):
                        if item == 1:
                            if y_pos + y < lock_shape[0] and x_pos + x < lock_shape[1] and y_pos + y > -1 and x_pos + x > -1:
                                key_plate[y_pos+y][x_pos+x] = 1
                if lock_in(key_plate, lock):
                    return True
    return False

def rotate_matrix_90_degrees(matrix):
    # 행렬의 크기 (정사각형 행렬이라고 가정)
    n = len(matrix)
    
    # 새로운 행렬 생성 (n x n)
    rotated_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]
    
    return rotated_matrix
    

def lock_in(key, lock):
    #k and l must have same shape(add padding.)
    for k, l in zip(key, lock):
        for k0, l0 in zip(k, l):
            if k0==0 and l0==1 :
                pass
            elif k0==1 and l0==0 :
                pass
            else:
                return False
    return True