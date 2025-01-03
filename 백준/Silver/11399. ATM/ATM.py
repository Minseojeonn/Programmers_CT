import sys

# 입력 처리

# 1 2 3 3 4
# = 1 + 3(1+2) + 6(1+2+3)  + 13 
temp = sys.stdin.readline()
sum_item = map(int, sys.stdin.readline().split())
sort_sum_item = sorted(sum_item)
result = 0
before_sum = 0
for i in sort_sum_item:
    before_sum = before_sum + i
    result = before_sum + result
print(result)

