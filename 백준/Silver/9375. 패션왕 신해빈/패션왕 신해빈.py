# 입을 수 있는 옷의 조합
# 의상의 수 0-30개
# 의상 이름, 종류 주어짐
# BFS로 풀 수 있나? 걍 조합 계싼이 빠를지도

num_test_case = int(input())
for _ in range(num_test_case):
    num_wearables = int(input())
    types_dict = {}
    comb_set = ()
    for _ in range(num_wearables):
        name, types = input().split(" ")
        if types in types_dict:
            types_dict[types].append(name)
        else:
            types_dict[types] = [name]

    answer = 1 
    for key in types_dict:
        answer = answer * (len(types_dict[key])+1)
        
    answer -= 1 #아무것도 없는 경우
    print(answer)