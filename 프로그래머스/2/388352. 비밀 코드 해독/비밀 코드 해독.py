from itertools import combinations
def first_input(n, first_q, first_ans):
    seed = list(combinations(first_q, first_ans))
    candidates = []
    remain_candidates = [i for i in range(1, n+1) if i not in first_q]
    seed2 = list(combinations(remain_candidates, 5-first_ans))
    for se in seed:
        for se2 in seed2:
            candidates.append(set(se+se2))
    return candidates
    
def solution(n, q, ans):
    candidates = first_input(n, q[0], ans[0])
    for idx, q_cand in enumerate(q[1:]):
        new_cand = []
        correct = ans[idx+1]
        for c in candidates:
            if len(c.intersection(set(q_cand))) == correct:
                new_cand.append(c)
        candidates=new_cand
    
    answer = len(candidates)
    return answer
