import sys

# 입력 처리
def figure_sign(su):
    if su == 0:
        print("0")
    elif su > 0:
        print("+")
    else:
        print("-")
for _ in range(3):
    din = int(sys.stdin.readline())
    temp_sum = 0
    for _ in range(din):
        temp_sum += int(sys.stdin.readline())
    figure_sign(temp_sum)
