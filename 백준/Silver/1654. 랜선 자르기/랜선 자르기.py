num_lan, need_lan = map(int, input().split(" "))
lan_list = []
for _ in range(num_lan):
    lan_list.append(int(input()))
lan_list.sort()

start = 1
end = lan_list[-1]

answer = 0
while start <= end:
    mid = (start+end)//2
    num_lan = 0
    for lan in lan_list:
        num_lan += lan // mid
    
    if num_lan >= need_lan:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)