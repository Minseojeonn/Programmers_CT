import math

def solution(n, w, num):
    # 1. 특정 번호의 박스가 몇 번째 줄(층), 몇 번째 칸(x)에 있는지 구하는 함수
    def get_coords(target_num, width):
        # 층 구하기 (0층부터 시작)
        row = (target_num - 1) // width
        # 해당 층 내에서의 순서 (0 ~ width-1)
        remainder = (target_num - 1) % width
        
        # 짝수 행(0, 2, 4...)은 왼쪽 -> 오른쪽
        if row % 2 == 0:
            xpos = remainder
        # 홀수 행(1, 3, 5...)은 오른쪽 -> 왼쪽
        else:
            xpos = (width - 1) - remainder
        return row, xpos

    # 2. 목표 박스와 마지막 박스의 위치 정보를 가져옴
    target_row, target_x = get_coords(num, w)
    last_row, last_x = get_coords(n, w)

    # 3. 기본적으로 목표 박스 위에 쌓인 층수 계산
    answer = last_row - target_row

    # 4. 마지막 층(최상단)에 목표 박스의 위치까지 박스가 차 있는지 확인
    # 마지막 층이 왼쪽->오른쪽 방향일 때
    if last_row % 2 == 0:
        if target_x > last_x: # 목표 위치가 마지막 박스보다 오른쪽에 있으면
            answer -= 1
    # 마지막 층이 오른쪽->왼쪽 방향일 때
    else:
        if target_x < last_x: # 목표 위치가 마지막 박스보다 왼쪽에 있으면 (숫자가 더 커지는 방향)
            answer -= 1
            
    return answer+1