line, value = input().split(" ")
matrix = []

matrix.append([0 for _ in range(int(value)+1)])
for i in range(int(line)):
    new_line = input().split(" ")
    new_line = [0] + new_line
    new_line = [int(i) for i in new_line]
    matrix.append(new_line)

for line in range(1,len(matrix)):
    for value in range(1,len(matrix[line])):
        matrix[line][value] += max(matrix[line-1][value-1], matrix[line-1][value], matrix[line][value-1])

print(matrix[-1][-1])