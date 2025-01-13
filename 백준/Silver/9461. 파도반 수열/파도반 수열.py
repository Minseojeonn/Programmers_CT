import sys

input_pos = []
start_line = [1, 1, 1]
for i in range(int(sys.stdin.readline().strip())):
    target = int(sys.stdin.readline().strip())
    if target < len(start_line)-1:
        pass
    else:
        for j in range(len(start_line), target+1):
            start_line.append(start_line[j-3] + start_line[j-2])
    print(start_line[target-1])