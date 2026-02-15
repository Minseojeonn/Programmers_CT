import math
num_user = int(input())
t_size = list(map(int, input().split()))
hold = list(map(int, input().split()))
t_hold = 0
pen_hold, individual = 0, 0
for i in t_size:
    t_hold += math.ceil(i/hold[0])

pen_hold = num_user // hold[1]
individual = num_user % hold[1]

print(t_hold)
print(f"{pen_hold} {individual}")