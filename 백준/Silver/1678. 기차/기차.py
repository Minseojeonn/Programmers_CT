import sys

num_train, first_arrive, num_station = map(int, sys.stdin.readline().strip().split())
arrive_list = []
train_name_dict = {}
for i in range(num_train):
    line_input = sys.stdin.readline().strip().split()
    train_name = line_input[0]
    train_name_dict[i] = train_name
    arrive_time = line_input[1:-1]
    for time in arrive_time:
        arrive_list.append((int(time), i))
ride_idx = -float("inf")
arrive_list = sorted(arrive_list, key=lambda x: x[0])
for idx, i in enumerate(arrive_list):
    temp_arrive, _ = i
    if temp_arrive >= first_arrive:
        ride_idx = idx
        break
if ride_idx == -float("inf"):
    ride_idx = 0
print(train_name_dict[arrive_list[(ride_idx + num_station - 1)%len(arrive_list)][1]])