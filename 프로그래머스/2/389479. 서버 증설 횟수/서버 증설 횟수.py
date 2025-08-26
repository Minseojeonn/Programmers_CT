def solution(players, m, k):
    improv = 0
    wall_clock = k
    indure = m
    
    on_server = []
    for time, i in enumerate(players):
        pivot = 0
        for end_time in on_server:
            if end_time > time:
                break
            else:
                pivot += 1
        on_server = on_server[pivot:]
        
        if i >= (len(on_server)+1) * indure:
            while True:
                on_server.append(time + wall_clock)
                improv += 1
                if i < (len(on_server)+1) * indure:
                    break
 
            
    
    return improv