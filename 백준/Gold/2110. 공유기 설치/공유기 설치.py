num_house, num_router = map(int, input().split(" "))
house_position = []
for _ in range(num_house):
    house_position.append(int(input()))

house_position.sort()
start = 1
end = abs(house_position[0] - house_position[-1])

while start <= end:
    mid = (end + start) // 2
    installed_router = 1
    last_installed = house_position[0]
    for h_pos in range(1, len(house_position)):
        if abs(house_position[h_pos] - last_installed) >= mid:
            installed_router += 1
            last_installed = house_position[h_pos]

    if num_router <= installed_router:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(answer)

 