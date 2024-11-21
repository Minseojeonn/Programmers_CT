import sys
from collections import defaultdict

# 입력 처리
num_case = int(sys.stdin.readline())
for i in range(num_case):
    loop_result = defaultdict(int)
    target = int(sys.stdin.readline())
    candidate = 2
    while True:
        if target == 1:
            break
        while target % candidate == 0:
            target = target / candidate
            loop_result[candidate] += 1
        candidate += 1
    for i in loop_result:
        print(i, loop_result[i])
