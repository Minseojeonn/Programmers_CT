remain_days = int(input())
schedule = []
global max_earn 
max_earn = 0
for i in range(remain_days):
    schedule.append(list(map(int, input().split())))

def back_tracking(days, cost):
    global max_earn 
    if days > remain_days-1:
        max_earn = max(max_earn, cost)
        return 
    else:
        spend_time, pay = schedule[days] 
        # pass
        back_tracking(days+1, cost)
        # accepted
        if spend_time + days - 1 < remain_days :
            back_tracking(spend_time + days, cost + pay)
    
back_tracking(0, 0)

print(max_earn)