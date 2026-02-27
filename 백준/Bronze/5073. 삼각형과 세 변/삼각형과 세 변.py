# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우

import sys

while True:
    edge = list(map(int, input().split(" ")))
    if sum(edge) == 0:
        break
    edge.sort()
    dicte = {}
    a, b, c = edge
    if c >= a+b:
        print("Invalid")
    else:
        for i in edge:
            if i in dicte:
                dicte[i]+=1
            else:
                dicte[i] = 1
    
        if len(dicte) == 1:
            print("Equilateral")
        elif len(dicte) == 2:
            print("Isosceles")
        elif len(dicte) == 3:
            print("Scalene")
    
