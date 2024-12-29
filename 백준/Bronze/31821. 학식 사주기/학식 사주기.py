import sys

"""
문제 
    결제 금액 총액
입력
    - 메뉴 개수 N 
        N개의 줄에 걸처 메뉴의 가격
    - 인원수 M
        M개의 줄에 걸쳐 먹고싶어 하는 메뉴의 번호.
문제 해결 방법
    Dict 혹은 List로 해결.
선택 방식 
    List로 해결.
    List의 index가 key임으로  List로도 O(1) 시간에 접근 가능.
    즉 메모리 더 사용하는 Dict를 쓸 필요가 없음. 
"""

# 입력 처리
menu_price = []
for i in range(int(sys.stdin.readline())):
    menu_price.append(int(sys.stdin.readline()))
overall_price = 0
for i in range(int(sys.stdin.readline())):
    overall_price += menu_price[int(sys.stdin.readline())-1]
    
print(overall_price)