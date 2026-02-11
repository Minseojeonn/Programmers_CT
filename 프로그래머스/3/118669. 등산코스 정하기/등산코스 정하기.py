import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))

    gates_set = set(gates)
    summits_set = set(summits)

    INF = 10**9
    best = [INF] * (n+1)

    pq = []
    for g in gates:
        best[g] = 0
        heapq.heappush(pq, (0, g))

    while pq:
        cur, u = heapq.heappop(pq)
        if cur != best[u]:
            continue

        # summit에 도달했으면, 왕복이든 편도든 intensity 최소값 계산엔 더 확장할 필요 없음
        # (왕복은 역으로 돌아올 수 있으니 intensity 값은 동일하게 성립)
        if u in summits_set:
            continue

        for v, w in graph[u]:
            nxt = max(cur, w)
            if nxt < best[v]:
                best[v] = nxt
                heapq.heappush(pq, (nxt, v))

    # summit 선택: intensity 최소, 동률이면 summit 번호 작은 것
    ans_s, ans_i = -1, INF
    for s in sorted(summits):
        if best[s] < ans_i:
            ans_s, ans_i = s, best[s]

    return [ans_s, ans_i]