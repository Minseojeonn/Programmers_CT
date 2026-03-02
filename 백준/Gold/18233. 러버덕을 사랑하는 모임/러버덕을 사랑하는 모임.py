from itertools import combinations

num_user, num_target, target_sum = map(int, input().split(" "))
scope = []
answer = None
for _ in range(num_user):
   scope.append(list(map(int,input().split(" "))))
for user_idxs in combinations(range(0, len(scope)), num_target):
    min_sum = 0
    max_sum = 0
    for uidx in user_idxs:
        min_user, max_user = scope[uidx]
        min_sum += min_user
        max_sum += max_user
    if min_sum <= target_sum <= max_sum:
        answer = [0] * num_user
        remain_duck = target_sum
        for uidx in user_idxs:
            answer[uidx] = scope[uidx][0]
            remain_duck = remain_duck - scope[uidx][0]
        while remain_duck >= 1:
            for uidx in user_idxs:
                if answer[uidx] <= scope[uidx][1]:
                    remain_user_duck = scope[uidx][1] - answer[uidx]
                    if remain_user_duck >= remain_duck:
                        answer[uidx] = answer[uidx] + remain_duck
                        remain_duck = 0
                        break
                    else:
                        answer[uidx] = answer[uidx] + remain_user_duck
                        remain_duck = remain_duck - remain_user_duck
        break
if answer == None:
    print(-1)
else:
    print(" ".join(map(str,answer)))

   


