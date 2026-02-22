from collections import deque

first = deque(list(map(int,[i for i in input()])))
second = deque(list(map(int,[i for i in input()])))
third = deque(list(map(int,[i for i in input()])))
fourth = deque(list(map(int,[i for i in input()])))

global wheels 
wheels = [first, second, third, fourth]
moved = [False, False, False, False]
left_connection = 6
right_connection = 2
# 극이 다르면, 반대방향으로 회전 같으면 스테이
def move(target_num, spin): #way 0 : both, way 1 : right, way -1 : left 
    if moved[target_num] == False:
        moved[target_num] = True
        target_left_sign = wheels[target_num][left_connection]
        target_right_sign = wheels[target_num][right_connection]
        
        if spin == -1:
            out = wheels[target_num].popleft()
            wheels[target_num].append(out)
        elif spin == 1: #타겟은 반시계, 근처는 시계
            out = wheels[target_num].pop()
            wheels[target_num].insert(0, out)
        
        if target_num != 0 and moved[target_num-1] == False:
            target_left_wheel_right_sign = wheels[target_num-1][right_connection]
            if target_left_wheel_right_sign != target_left_sign:
                move(target_num-1, spin * -1)
            else:
                moved[target_num-1] = True
        
        if target_num != 3 and moved[target_num+1] == False:
            target_right_wheel_left_sign = wheels[target_num+1][left_connection]
            if target_right_wheel_left_sign != target_right_sign:
                move(target_num+1, spin * -1)
            else:
                moved[target_num+1] = True
    else:
        pass  
    
for i in range(int(input())):
    number, direction = map(int, input().split())
    moved = [False, False, False, False]
    move(number-1, direction)

print(first[0] + second[0] * 2 + third[0] * 4 + fourth[0] * 8)