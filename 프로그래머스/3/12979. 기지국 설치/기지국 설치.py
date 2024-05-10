import math
def solution(n, stations, w):
    answer = 0
    end = 0
    for station in stations:
        if station - end > 1:
            answer += math.ceil((station - w - end - 1)/(w*2+1))
            end = station + w 
        else:
            end = station + w
    if end < n:
        left = n - end 
        answer += math.ceil(left/(w*2+1))
    print(end)
    return answer