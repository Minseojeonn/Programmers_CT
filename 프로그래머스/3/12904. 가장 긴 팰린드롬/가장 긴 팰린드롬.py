def two_pointer(s,front,back):
    same_count = 0
    while front <= back:
        if s[front] == s[back]:
            front += 1
            back -= 1
            if front == back:
                same_count += 1
            else:
                same_count += 2
            continue
        else:
            return -1
    return same_count
    
def solution(s):
    answer = 0
    for idx in range(len(s)): #front
        for jdx in range(idx+1,len(s)): #back
            if s[idx] == s[jdx]:
                length = two_pointer(s,idx,jdx) 
                if length > 0:
                    answer = max(length, answer)
                    if jdx == len(s)-1: #early stop
                        return answer
    if answer == 0:
        answer = 1
    return answer