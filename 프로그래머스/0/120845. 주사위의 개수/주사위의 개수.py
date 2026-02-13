def solution(box, n):
    answer = 0
    # 가로, 세로, 높이 box, 주사위 모서리 길이 정수 n, 이때 주사위는 정육면체
    
    row, col, height = box
    
    answer = (row//n) * (col//n) * (height//n)
    return answer