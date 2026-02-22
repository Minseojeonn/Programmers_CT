import copy
num_user = int(input())
global min_diff
min_diff = float("inf")
adj_matrix = []
for i in range(num_user):
    adj_matrix.append(list(map(int,input().split())))
    
def backtacking(team_a_cost, team_b_cost, team_a, team_b, user_idx):
    global min_diff
    if len(team_a) == num_user//2 and len(team_b) == num_user//2:
        min_diff = min(abs(team_a_cost - team_b_cost), min_diff)
    else:
        if len(team_a) < num_user // 2:
            added_cost = 0
            added_user_idx = user_idx + 1
            for person in team_a:
                added_cost += adj_matrix[added_user_idx][person]
                added_cost += adj_matrix[person][added_user_idx]
            temp_team_a = copy.deepcopy(team_a)
            temp_team_a.append(added_user_idx)
            backtacking(team_a_cost + added_cost, team_b_cost, temp_team_a, team_b, user_idx+1)
            
        if len(team_b) < num_user // 2:
            added_cost = 0
            added_user_idx = user_idx + 1
            for person in team_b:
                added_cost += adj_matrix[added_user_idx][person]
                added_cost += adj_matrix[person][added_user_idx]
            temp_team_b = copy.deepcopy(team_b)
            temp_team_b.append(added_user_idx)
            backtacking(team_a_cost, team_b_cost + added_cost, team_a, temp_team_b, user_idx+1)
            
backtacking(0, 0, [], [], -1)

print(min_diff)