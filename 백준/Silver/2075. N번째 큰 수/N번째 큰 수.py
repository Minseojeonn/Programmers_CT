import heapq
x_len = int(input())

p_queue = []
for i in range(x_len):
    input_row = list(map(int, input().split(" ")))
    for j in input_row:
        heapq.heappush(p_queue, j)
        if len(p_queue) == x_len+1:
            heapq.heappop(p_queue)
            
print(p_queue[0])