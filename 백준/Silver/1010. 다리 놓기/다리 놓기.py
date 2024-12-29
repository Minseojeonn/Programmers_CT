import sys

# 입력 처리


dic = {}
def result(left, right):
    if left == right:
        return 1
    elif left == 1:
        return right
    else:
        if (left,right) in dic:
            return dic[(left,right)]
        else:
            sum = 0
            for i in range(left-1, right):
                sum = sum + result(left-1, i)
            dic[(left,right)] = sum
            return sum    

for i in range(int(sys.stdin.readline())):
    left, right = map(int, sys.stdin.readline().split())
    print(result(left,right))
