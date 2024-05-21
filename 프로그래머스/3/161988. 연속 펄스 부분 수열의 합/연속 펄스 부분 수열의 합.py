def multi(sequence,start_with):
    line = []
    for i in sequence:
        line.append(i*start_with)
        start_with *= -1
    return line
def solution(sequence):
    m1_seq = multi(sequence,-1)
    p1_seq = multi(sequence,1)
    answer = 0
    temp_sum = 0
    for i in m1_seq:
        temp_sum += i
        if temp_sum <= 0:
            temp_sum = 0
        else:
            answer = max(temp_sum, answer)
    temp_sum = 0
    for i in p1_seq:
        temp_sum += i
        if temp_sum <= 0:
            temp_sum = 0
        else:
            answer = max(temp_sum, answer)

    return answer