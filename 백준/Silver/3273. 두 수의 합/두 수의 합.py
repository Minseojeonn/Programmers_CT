import sys
from itertools import permutations

_ = int(sys.stdin.readline().strip())
sequence = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline().strip())
answer = 0
sequence = sorted(sequence)
front = 0
back = 0


for i in range(len(sequence)):
    for j in range(i+1, len(sequence)):
        if sequence[i] + sequence[j] == target:
            answer += 1
        if sequence[i] + sequence[j] > target:
            break
print(answer)
    
