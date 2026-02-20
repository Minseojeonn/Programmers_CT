import copy
from collections import deque
scope, length = map(int, input().split())

candid_list = [i for i in range(1, scope+1)]

if length == 1:
    for i in range(1, scope+1):
        print(i)
else:
    for i in range(1,scope+1):
        copy_candid_list = copy.deepcopy(candid_list)
        copy_candid_list.remove(i)
        queue = deque([([i], copy_candid_list)])
        while queue:
            next_per = queue.popleft()
            past, future = next_per
            for fu in future:
                candid_past = past + [fu]
                rest_future = copy.deepcopy(future)
                rest_future.remove(fu)
                if len(candid_past) == length:
                    print(" ".join(list(map(str,candid_past))))
                else:
                    queue.append((candid_past, rest_future))
                
            
