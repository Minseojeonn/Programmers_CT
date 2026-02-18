from collections import deque

def find_unvisited(picture, visited):
    for idx, i in enumerate(visited):
        for jdx, j in enumerate(i):
            if j == 0:
                return (idx, jdx, picture[idx][jdx]) 
    
num_rows = int(input())
picture = []
for i in range(num_rows):
    temp_list = []
    for j in input():
        temp_list.append(j)
    picture.append(temp_list)
normal_visited = []
abnormal_visited = []
for i in picture:
    temp_list = []
    temp_list2 = []
    for j in i:
        temp_list.append(0)
        temp_list2.append(0)
    normal_visited.append(temp_list)
    abnormal_visited.append(temp_list2)

#queue for normal
num_cluster_for_normal = 0
while all([0 not in row for row in normal_visited])==False:
    num_cluster_for_normal += 1
    normal_queue = deque([])
    normal_queue.append(find_unvisited(picture, normal_visited))
    normal_visited[normal_queue[0][0]][normal_queue[0][1]] = 1
    while normal_queue:
        next_y, next_x, next_color = normal_queue.popleft()
        for dy, dx in zip([0, 0, -1, 1],[-1, 1, 0, 0]):
            if  -1 < next_y+dy < len(picture) and -1 < next_x + dx < len(picture[0]):
                if next_color == picture[next_y+dy][next_x+dx] and normal_visited[next_y+dy][next_x + dx] == 0:
                    normal_visited[next_y+dy][next_x + dx] = 1
                    normal_queue.append((next_y+dy, next_x+dx, picture[next_y+dy][next_x+dx]))
                    

for idx, i in enumerate(picture):
    for jdx, j in enumerate(i):
        if j == "G":
            picture[idx][jdx] = "R"

num_cluster_for_abnormal = 0
while all([0 not in row for row in abnormal_visited])==False:
    num_cluster_for_abnormal += 1
    abnormal_queue = deque([])
    abnormal_queue.append(find_unvisited(picture, abnormal_visited))
    abnormal_visited[abnormal_queue[0][0]][abnormal_queue[0][1]] = 1
    while abnormal_queue:
        next_y, next_x, next_color = abnormal_queue.popleft()
        for dy, dx in zip([0, 0, -1, 1],[-1, 1, 0, 0]):
            if  -1 < next_y+dy < len(picture) and -1 < next_x + dx < len(picture[0]):
                if next_color == picture[next_y+dy][next_x+dx] and abnormal_visited[next_y+dy][next_x + dx] == 0:
                    abnormal_visited[next_y+dy][next_x + dx] = 1
                    abnormal_queue.append((next_y+dy, next_x+dx, picture[next_y+dy][next_x+dx]))


print(num_cluster_for_normal, num_cluster_for_abnormal)