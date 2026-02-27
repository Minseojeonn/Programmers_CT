num_users, len_logs = map(int, input().split(" "))
roll_dict = {}

for i in range(len_logs):
    user_id = input()
    roll_dict[user_id] = i

listin = []

for i in roll_dict:
    listin.append((roll_dict[i], i))
    
listin.sort()

for i in listin[:num_users]:
    print(i[1])

    

    
    


