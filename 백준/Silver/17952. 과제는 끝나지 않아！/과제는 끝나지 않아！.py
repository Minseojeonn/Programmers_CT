num_mins = int(input())
homework_stack = []
get_score = 0
for _ in range(num_mins):
   
    input_list = list(map(int, input().split(" ")))
    if len(input_list) == 1: #no homework
        pass
    else: # yes homework
        action, score, need_time = input_list
        homework_stack.append((score, need_time))
    if homework_stack:
        homework_stack[-1] = (homework_stack[-1][0], homework_stack[-1][1]-1)
        if homework_stack[-1][1] == 0:
            end_score, _ = homework_stack.pop()
            get_score = get_score + end_score

print(get_score)