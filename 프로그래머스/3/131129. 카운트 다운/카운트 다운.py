def solution(target):
    INF = 10**9

    throws = []
    for mul in (1, 2, 3):
        for num in range(1, 21):
            val = mul * num
            is_single = 1 if mul == 1 else 0
            throws.append((val, is_single))
    throws.append((50, 1))  # bull

    # dp_darts[s] = 최소 다트 수
    # dp_single[s] = 그 최소 다트 수에서 single/bull 최대
    dp_darts = [INF] * (target + 1)
    dp_single = [-INF] * (target + 1)

    dp_darts[0] = 0
    dp_single[0] = 0

    for curr_score in range(target + 1):
        if dp_darts[curr_score] == INF:
            continue
        
        for throw in throws:
            score, issingle = throw
            next_score = curr_score + score
            if next_score > target:
                continue
            
            next_darts=dp_darts[curr_score]+1
            next_single=dp_single[curr_score]+issingle
            
            if next_darts < dp_darts[next_score]:
                dp_darts[next_score] = next_darts
                dp_single[next_score] = next_single
            elif next_darts == dp_darts[next_score] and next_single > dp_single[next_score]:
                dp_single[next_score] = next_single
                
                
    

    return [dp_darts[target], dp_single[target]]