import sys
import math

num_test_case = int(sys.stdin.readline())

for _ in range(num_test_case):
    start, end = map(int, sys.stdin.readline().split())
    distance = end - start
    
    if distance == 0:
        print(0)
        continue
        
    # 거리의 제곱근을 구해서 정수형으로 변환 (n)
    n = int(math.isqrt(distance))
    
    if distance == n ** 2:
        print(2 * n - 1)
    elif distance <= n ** 2 + n:
        print(2 * n)
    else:
        print(2 * n + 1)