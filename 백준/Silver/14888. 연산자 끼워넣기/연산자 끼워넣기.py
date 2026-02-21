gabage = input()
int_list = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
global answer_list 
answer_list = []

def backtracking(int_list, depth, local_sum, local_plus, local_minus, local_multi, local_div):
    global answer_list
    if depth == len(int_list)-1:
        answer_list.append(local_sum)
    else:
        if local_plus > 0:
            candid_sum = local_sum + int_list[depth+1]
            backtracking(int_list, depth+1, candid_sum, local_plus-1, local_minus, local_multi, local_div)
        if local_minus > 0:
            candid_sum = local_sum - int_list[depth+1]
            backtracking(int_list, depth+1, candid_sum, local_plus, local_minus-1, local_multi, local_div)
        if local_multi > 0:
            candid_sum = local_sum * int_list[depth+1]
            backtracking(int_list, depth+1, candid_sum, local_plus, local_minus, local_multi-1, local_div)
        if local_div > 0:
            if local_sum < 0:
                candid_sum = -(abs(local_sum)//int_list[depth+1])
            else: 
                candid_sum = local_sum // int_list[depth+1]
            
            backtracking(int_list, depth+1, candid_sum, local_plus, local_minus, local_multi, local_div-1)

backtracking(int_list, 0, int_list[0], plus, minus, multi, div)
print(max(answer_list))
print(min(answer_list))