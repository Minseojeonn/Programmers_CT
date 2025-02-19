import sys

N, K = list(map(int,sys.stdin.readline().strip().split()))

mapp = []
for i in range(N):
    temp = [s for s in str(sys.stdin.readline().strip())]
    mapp.append(temp)

#indexing은 양쪽다 -1임
#항상 성립하기때문에, 예외처리 X
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(mapp):
    stack = []
    visited = [[0]*K for _ in range(N)]    
    visited[0][0] = 1
    stack.append((0,0,1)) # (row, col, cnt)
    while stack:
        row, col, cnt = stack.pop(0)
        if row == N-1 and col == K-1:
            print(cnt)
            return 0
        for ddx, ddy in zip(dx, dy):
            if row+ddy >= 0 and row+ddy < N and col+ddx >= 0 and col+ddx < K:
                if visited[row+ddy][col+ddx] == 0 and mapp[row+ddy][col+ddx] == '1':
                    visited[row+ddy][col+ddx] = 1
                    stack.append((row+ddy, col+ddx, cnt+1))
                  
dfs(mapp)