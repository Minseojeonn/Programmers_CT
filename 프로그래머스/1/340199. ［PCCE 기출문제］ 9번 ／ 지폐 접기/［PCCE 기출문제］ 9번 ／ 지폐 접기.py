def solution(wallet, bill):
    answer = 0
    while True:
        if max(wallet) >= max(bill) and min(wallet) >= min(bill):
            break
        else:
            bill = [max(bill) // 2, min(bill)]
        answer += 1
    return answer