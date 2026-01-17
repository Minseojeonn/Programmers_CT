def solution(info, n, m):
    INF = 10**15
    L = len(info)

    # best[turn][Bcost] = 그 상태에서의 최소 Acost
    best = [ [INF]*m for _ in range(L+1) ]
    best[0][0] = 0

    stack = [(0, 0, 0)]  # (turn, Acost, Bcost)

    while stack:
        turn, Acost, Bcost = stack.pop()

        if turn == L:
            continue

        a, b = info[turn]

        # A가 훔침
        na = Acost + a
        if na < n and na < best[turn+1][Bcost]:
            best[turn+1][Bcost] = na
            stack.append((turn+1, na, Bcost))

        # B가 훔침
        nb = Bcost + b
        if nb < m and Acost < best[turn+1][nb]:
            best[turn+1][nb] = Acost
            stack.append((turn+1, Acost, nb))

    ans = min(best[L])
    return -1 if ans == INF else ans