# 동전 N종류, 동전 개수 제한 없음
# 가치의 합 K로 만들것. 필요한 동전 개수의 최소값.
# 최소값이면.. dp?로 메모리 초과네..
num_types, target_cost = map(int, input().split(" "))
coins = []
for i in range(num_types):
    coins.append(int(input()))
    
answer = 0    
for i in range(num_types-1, -1, -1):
    if target_cost == 0:
        break
    if target_cost >= coins[i]:
        answer += target_cost // coins[i]
        target_cost = target_cost % coins[i]
        
print(answer)