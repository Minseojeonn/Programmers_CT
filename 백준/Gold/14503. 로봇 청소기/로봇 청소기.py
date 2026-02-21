import sys
input = sys.stdin.readline

ylen, xlen = map(int, input().split())
y, x, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(ylen)]

# 북(0), 동(1), 남(2), 서(3) 순서에 따른 dy, dx
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0

while True:
    # 1. 현재 칸이 청소되지 않은 경우
    if maps[y][x] == 0:
        maps[y][x] = -1 # 청소 완료 표시
        answer += 1
    
    # 주변 4칸 확인
    surround_empty = False
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < ylen and 0 <= nx < xlen:
            if maps[ny][nx] == 0:
                surround_empty = True
                break
    
    # 2. 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
    if not surround_empty:
        # 후진: 현재 방향(d)의 반대 방향으로 이동
        # 북(0) -> 남(2), 동(1) -> 서(3) ... 즉, (d+2)%4
        back_y, back_x = y - dy[d], x - dx[d]
        
        if 0 <= back_y < ylen and 0 <= back_x < xlen and maps[back_y][back_x] != 1:
            y, x = back_y, back_x
        else: # 뒤가 벽이라 후진 못하면 종료
            break
            
    # 3. 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
    else:
        # 반시계 방향으로 90도 회전
        d = (d - 1) % 4
        # 앞쪽 칸 확인
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < ylen and 0 <= nx < xlen and maps[ny][nx] == 0:
            y, x = ny, nx

print(answer)