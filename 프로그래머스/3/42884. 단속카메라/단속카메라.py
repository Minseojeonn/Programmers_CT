def solution(routes):
    #모든 차량이 한 번은 단속용 카메라를 만나야 한다.
    #일단은 소팅 하자.
    routes = sorted(routes, key=lambda x:x[0])
    before_end = routes[0][1]
    answer = 1
    for car in routes[1:]:
        route_strat = car[0]
        route_end = car[1]
        #print(route_strat, route_end, before_end)
        if before_end >= route_strat:
            if before_end > route_end:
                before_end = min(route_end,before_end)
            else:
                pass
        else:
            before_end = route_end
            answer += 1
        
    
    return answer