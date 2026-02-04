#16:17 start
from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    discount = [10, 20, 30, 40]
    
    for comb in product(discount, repeat=len(emoticons)): #for all discount case
        comb_all_money = 0
        num_member = 0
        for user in users: #for all users
            u_pivot, budget = user
            user_all_money = 0
            for idx, dis in enumerate(comb):  # for all items 
                if dis >= u_pivot:
                    user_all_money += emoticons[idx] * ((100-dis)/100)
            if user_all_money >= budget:
                num_member +=1
            else:
                comb_all_money += user_all_money
            
        if answer[0] <= num_member:
            if answer[0] == num_member:
                answer[1] = max(answer[1], comb_all_money)
            else:
                answer[0] = num_member
                answer[1] = comb_all_money
    
    return answer