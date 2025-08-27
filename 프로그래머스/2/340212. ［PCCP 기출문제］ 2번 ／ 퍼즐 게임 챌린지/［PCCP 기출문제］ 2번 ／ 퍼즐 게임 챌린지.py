def solution(diffs, times, limit):
    def calculate(diffs, times, level):
        solving_time = sum(times)
        for idx, diff in enumerate(diffs):
            if diff > level:
                solving_time += (times[idx-1] + times[idx]) * (diff - level)
        return solving_time

    left, right = 1, max(diffs)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        solve_time = calculate(diffs, times, mid)
        #print(mid, solve_time)
        if solve_time > limit:   # 조건 만족
                      # 후보 갱신
            left = mid + 1         # 더 큰 level 시도
        else:     
            answer = mid # 조건 불만족
            right = mid - 1

    return answer