import sys
#문제
##초콜릿은 NxM으로 쪼개져 있음
##1x1 크기의 초콜릿으로 쪼개기 위한 최소 쪼개기 횟수

#입력
#한줄로 정수 N, M [1,300]

#출력
#첫째줄에 답

# 입력 처리
row, col = map(int, sys.stdin.readline().split())

#문제 구체화
#한 방향으로 싹 자르고, 곱해준다 다음거에
print((row-1) + ((col-1) * row)) 
 