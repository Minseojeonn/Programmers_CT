import sys

# input을 sys.stdin.readline으로 교체 (속도 향상의 핵심)
input = sys.stdin.readline

num_loop = int(input())

for _ in range(num_loop):
    num_team, num_probm, my_team_id, num_log = map(int, input().split())
    my_team_id = my_team_id - 1
    
    # 각 팀별 문제 점수를 저장 (문제당 최대 점수만 유지)
    score_list = [[0] * num_probm for _ in range(num_team)]
    # 제출 횟수와 마지막 제출 시간을 저장할 리스트 (딕셔너리보다 리스트가 더 빠름)
    submit_cnt = [0] * num_team
    last_submit_time = [0] * num_team
    
    for log_idx in range(num_log):
        log_team_id, log_num_probm, log_get_score = map(int, input().split())
        t_idx = log_team_id - 1
        p_idx = log_num_probm - 1
        
        # 1. 최고 점수 갱신
        if score_list[t_idx][p_idx] < log_get_score:
            score_list[t_idx][p_idx] = log_get_score
            
        # 2. 제출 횟수 증가 및 시간 기록
        submit_cnt[t_idx] += 1
        last_submit_time[t_idx] = log_idx

    # 내 팀의 기준 정보 추출
    my_score = sum(score_list[my_team_id])
    my_submit = submit_cnt[my_team_id]
    my_last_summit = last_submit_time[my_team_id]
    
    good_team = 1
    for i in range(num_team):
        if i == my_team_id:
            continue
            
        other_score = sum(score_list[i])
        
        # 순위 비교 로직 (작성하신 내용과 동일)
        if other_score > my_score:
            good_team += 1
        elif other_score == my_score:
            if submit_cnt[i] < my_submit:
                good_team += 1
            elif submit_cnt[i] == my_submit:
                if last_submit_time[i] < my_last_summit:
                    rank_up = True
                    good_team += 1
    
    print(good_team)