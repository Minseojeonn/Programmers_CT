def solution(scores):
    scores_sorted = sorted(scores, key=lambda x:(-x[0], x[1]))
    max_back = -1
    rank, wanho_sum = 1, sum(scores[0])

    for f, b in scores_sorted:
        if f > scores[0][0] and b > scores[0][1]:
            return -1
        if b >= max_back:
            if (f, b) != scores[0] and f + b > wanho_sum:
                rank += 1
            max_back = max(max_back, b)
    return rank

# 1. 완호의 석차만 출력하면 됨.
# 5 4 6 2