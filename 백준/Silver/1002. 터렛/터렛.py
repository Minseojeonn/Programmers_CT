# 마린의 위치를 계산할것.
# 각자 자신의 터렛에서, 마린까지의 거리 계산.
# 터렛 A와 B의 좌표가 주어지고, A가 계산한 거리및 B가 계산한 거리가 주어짐.
# 이때, 마린이 존재할 수 있는 좌표 계산할것.

num_test_case = int(input())
for _ in range(num_test_case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(" "))
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    added, minus = r1 + r2, abs(r1-r2)
    if distance == 0 :
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif distance == added or distance == minus:
        print(1)
    else:
        if minus < distance <= added:
            print(2)
        else:
            print(0)
    
        
