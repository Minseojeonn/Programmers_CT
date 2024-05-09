def solution(A, B):
    B = sorted(B)
    A = sorted(A)
    answer = 0
    while A and B:
        if A[-1] < B[-1]:
            answer += 1
            A.pop()
            B.pop()
        else:
            A.pop()
    return answer