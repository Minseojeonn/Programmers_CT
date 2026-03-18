import sys
import heapq

# 입력 속도 향상 (코테 필수)
input = sys.stdin.readline

len_size = int(input())
matrix = [list(map(int, input().split())) for _ in range(len_size)]

# N이 1인 경우 예외 처리
if len_size == 1:
    print(0)
    sys.exit()

# 비용 무한대 배열 설정
height_matrix = [[float('inf')] * len_size for _ in range(len_size)]
height_matrix[0][0] = 0

# heapq 사용 (max_cost가 작은 순서대로 pop 되도록 첫 번째 원소에 max_cost 배치)
pq = []
heapq.heappush(pq, (0, 0, 0)) # (max_cost, current_y, current_x)

while pq:
    max_cost, current_y, current_x = heapq.heappop(pq)
    
    # 목표 지점에 도달하면 즉시 종료 (우선순위 큐 덕분에 이때의 max_cost가 무조건 최소값)
    if current_y == len_size - 1 and current_x == len_size - 1:
        print(max_cost)
        break

    # 이미 더 적은 비용으로 방문 처리된 곳이라면 스킵 (시간 단축의 핵심)
    if max_cost > height_matrix[current_y][current_x]:
        continue

    # 4방향 탐색
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        candid_y, candid_x = current_y + dy, current_x + dx
        
        if 0 <= candid_y < len_size and 0 <= candid_x < len_size:
            # 기존 max_cost와 다음 칸으로 갈 때의 경사 차이 중 큰 값 선택
            candid_max_cost = max(max_cost, abs(matrix[current_y][current_x] - matrix[candid_y][candid_x]))
            
            # 더 적은 최대 경사로 갈 수 있다면 갱신 후 힙에 push
            if candid_max_cost < height_matrix[candid_y][candid_x]:
                height_matrix[candid_y][candid_x] = candid_max_cost
                heapq.heappush(pq, (candid_max_cost, candid_y, candid_x))