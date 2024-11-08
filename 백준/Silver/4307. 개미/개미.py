import sys
num_case = int(input())
for i in range(num_case):
    length, num_ant = map(int, input().split())
    ant = [int(sys.stdin.readline()) for _ in range(num_ant)]
    half = length/2
    min_half = length+1  # 중앙에서 가장 가까운것
    max_half = 0  # 중앙에서 가장 먼 친구
    for j in ant:
        cal = abs(half-j)
        min_half = min(min_half, cal)
        max_half = max(max_half, cal)
    A = half - min_half
    B = half + max_half

    print(int(A), int(B))
