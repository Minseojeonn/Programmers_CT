import sys
import itertools
#init point
num_kit, decay = map(int, sys.stdin.readline().split())

kit = []
answer = 0
start_point = 500
for i in sys.stdin.readline().strip().split():
    kit.append(int(i))

candidate = itertools.permutations(kit, num_kit)
for i in candidate:
    start = 500
    fail = False
    for tool in i:
        start = start - decay + tool
        if start < 500:
            fail = True
            break
    if fail == False:
        answer += 1
        
print(answer)