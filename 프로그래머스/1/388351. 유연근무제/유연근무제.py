def solution(schedules, timelogs, startday):
    answer = 0
    for schedule, timelog in zip(schedules, timelogs):
        startday_cal = startday
        schedule_due = schedule + 10
        if schedule_due % 100 >= 60:
            schedule_due = schedule_due + 100 - 60
        is_pass = True
        for timelo in timelog:
            if startday_cal == 6 or startday_cal == 7:
                pass
            else:
                if schedule_due >= timelo:
                    pass
                else:
                    is_pass = False
            startday_cal += 1
            if startday_cal == 8:
                startday_cal = 1
        if is_pass:
            answer += 1
            
    return answer