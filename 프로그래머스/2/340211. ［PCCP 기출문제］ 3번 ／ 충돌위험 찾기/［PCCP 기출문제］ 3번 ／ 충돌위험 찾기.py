def simulation(robot_states):
    robot_position_row, robot_position_col = robot_states["pos"]
    target_position_row, target_position_col = robot_states["routes"][robot_states["visit_num"]]
    
    #move col
    if robot_position_row != target_position_row:
        diff_row = robot_position_row - target_position_row
        if diff_row > 0 :
             nex_pos_row, next_pos_col = robot_position_row-1, robot_position_col
        else:
             nex_pos_row, next_pos_col = robot_position_row+1, robot_position_col
    #move row
    else:
        diff_col = robot_position_col - target_position_col
        if diff_col > 0 :
             nex_pos_row, next_pos_col = robot_position_row, robot_position_col-1
        else:
             nex_pos_row, next_pos_col = robot_position_row, robot_position_col+1
    
    if [nex_pos_row, next_pos_col] == robot_states["routes"][robot_states["visit_num"]]:
        next_visit_num = robot_states["visit_num"]+1
    else:
        next_visit_num = robot_states["visit_num"]
        
    new_robot_states = {
            "pos" : [nex_pos_row, next_pos_col],
            "visit_num" : next_visit_num,
            "routes" : robot_states["routes"]
        } 
    return new_robot_states
    
def solution(points, routes):
    answer = 0
    robot = {}
    for idx, route in enumerate(routes):
        robot_states = {
            "pos" : points[route[0]-1],
            "visit_num" : 1,
            "routes" : [points[i-1] for i in route]
        }
        robot[idx] = robot_states
    
    duple_check = {}
    for robot_index in robot:
        if tuple(robot[robot_index]["pos"]) not in duple_check:
            duple_check[tuple(robot[robot_index]["pos"])] = 1
        else:
            duple_check[tuple(robot[robot_index]["pos"])] += 1
    
    crash = 0
    for key in duple_check:
        if duple_check[key] > 1:
            crash +=1
    answer += crash
    
    print(duple_check)
        
    while len(robot) != 0:
        
        for robot_index in list(robot.keys()):
            robot[robot_index] = simulation(robot[robot_index])
        
        duple_check = {}
        for robot_index in robot:
            if tuple(robot[robot_index]["pos"]) not in duple_check:
                duple_check[tuple(robot[robot_index]["pos"])] = 1
            else:
                duple_check[tuple(robot[robot_index]["pos"])] += 1
                
        crash = 0
        for key in duple_check:
            if duple_check[key] > 1:
                crash +=1
       # print(duple_check)
        answer += crash
            
        for robot_index in list(robot.keys()):
            if robot[robot_index]['visit_num'] == len(robot[robot_index]['routes']):
                del robot[robot_index] 
        
    return answer


