def solution(n, results):
    answer = 0
    adj = [[0 for _ in range(n)] for _ in range(n)]
    absadj = [[0 for _ in range(n)] for _ in range(n)]
    for i in results:
        to, fr = i
        adj[fr-1][to-1] = 1
        adj[to-1][fr-1] = -1
        absadj[fr-1][to-1] = 1
        absadj[to-1][fr-1] = 1
    
    idx = 0
    visited = {}
    while True:
        if idx not in visited and -1 in adj[idx]:
            visited[idx] = 1
            win_index = []
            lose_index = []
            for kdx, i  in enumerate(adj[idx]):
                if i == 1:
                    win_index.append(kdx)
                elif i == -1:
                    lose_index.append(kdx)
            idx = 0
            #print(win_index, lose_index)
            for li in lose_index:
                for wi in win_index:
                    absadj[li][wi] = 1
                    absadj[wi][li] = 1
                    adj[li][wi] = 1
                    adj[wi][li] = -1
        else:
            idx+=1
            if idx == n:
                break
        
    for idx,i in enumerate(absadj):
        #print(adj[idx])
        if sum(i) == n-1:
            answer+=1
                    
        
    
    return answer
