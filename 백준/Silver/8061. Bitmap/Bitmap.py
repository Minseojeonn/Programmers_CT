import sys
from collections import deque

# Input
row, col = map(int, sys.stdin.readline().split())

# Directions (right, left, down, up)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# Read the matrix
matrix = [list(sys.stdin.readline().strip()) for _ in range(row)]

# Distance matrix initialized to -1
distance = [[-1] * col for _ in range(row)]

# Queue for BFS
queue = deque()

# Initialize queue with all '1' positions
for y in range(row):
    for x in range(col):
        if matrix[y][x] == '1':
            queue.append((y, x))
            distance[y][x] = 0  # Distance to itself is 0

# Multi-source BFS
while queue:
    y, x = queue.popleft()
    for i in range(4):  # Check 4 directions
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < row and 0 <= nx < col and distance[ny][nx] == -1:
            distance[ny][nx] = distance[y][x] + 1
            queue.append((ny, nx))

# Output the result
for row in distance:
    print(" ".join(map(str, row)))