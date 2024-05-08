def solution(triangle):
    answer = 0
    dp = [[0 for _ in j] for j in triangle]
    for line_idx in range(len(triangle)):
        temp_line = triangle[line_idx]
        if line_idx == 0:
            dp[line_idx][0] = temp_line[0]
        else:
            for atom_idx in range(len(temp_line)):
                if atom_idx == 0:
                    dp[line_idx][atom_idx] = triangle[line_idx][atom_idx] + dp[line_idx-1][atom_idx]
                elif atom_idx == len(temp_line)-1:
                    dp[line_idx][atom_idx] = triangle[line_idx][atom_idx] + dp[line_idx-1][atom_idx-1]
                else:
                    dp[line_idx][atom_idx] = triangle[line_idx][atom_idx] + max(dp[line_idx-1][atom_idx], dp[line_idx-1][atom_idx-1])
            
    answer = max(dp[-1])
    return answer