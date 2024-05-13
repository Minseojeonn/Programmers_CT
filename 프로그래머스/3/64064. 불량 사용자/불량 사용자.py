def compare(candidate,j):
    if len(candidate) != len(j):
        return False
    for idx in range(min(len(candidate),len(j))):
        temp = j[idx]
        if j[idx] == "*":
            pass
        else:
            if j[idx] != candidate[idx]:
                return False
    return True
from collections import deque   
def solution(user_id, banned_id):
    answer = 0
    can_ban_list = []
    for ban in banned_id:
        ban_list = []
        for user in user_id:
            if compare(user,ban) :
                ban_list.append(user)
        if len(ban_list) > 0:
            can_ban_list.append(ban_list)
    
    can_ban_list = sorted(can_ban_list,key=lambda x:len(x))
    
    que = deque()
    for i in can_ban_list[0]:
        que.append(([i],0))
    answer_list = []
    while que:
        visited, turn = que.popleft()
        if turn+1 < len(can_ban_list):
            for i in can_ban_list[turn+1]:
                if i not in visited :
                    que.append((visited+[i],turn+1))
        else:
            if len(visited) == len(banned_id):
                if set(visited) not in answer_list:
                    answer_list.append(set(visited))
    return len(answer_list)