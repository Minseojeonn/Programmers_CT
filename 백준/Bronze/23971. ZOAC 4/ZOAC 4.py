import math
y_size, x_size, y_gap, x_gap = map(int, input().split(" "))

num_y = math.ceil((y_size) / (1 + y_gap))
num_x = math.ceil((x_size) / (1 + x_gap))
print(num_y*num_x)