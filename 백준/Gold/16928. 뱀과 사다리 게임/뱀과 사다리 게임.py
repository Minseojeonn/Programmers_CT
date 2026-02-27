import heapq
num_ladder, num_snail = map(int, input().split(" "))
trick = {}
visited = [9999999] * 101

for ladder in range(num_ladder):
    fr, to = map(int, input().split(" "))
    trick[fr] = to

for snail in range(num_snail):
    fr, to = map(int, input().split(" "))
    trick[fr] = to

p_queue = [(0, 1)] #move, pos
answer = 0
while p_queue:
    cur_move, cur_pos = heapq.heappop(p_queue)
    if cur_pos == 100:
        answer = cur_move
        break
    for i in range(1, 7):
        cand_pos = i+cur_pos
        if cand_pos in trick:
            cand_pos = trick[cand_pos]
        if cand_pos <= 100 and visited[cand_pos] > cur_move+1:
            visited[cand_pos] = cur_move+1
            heapq.heappush(p_queue, (cur_move+1, cand_pos))

print(answer)