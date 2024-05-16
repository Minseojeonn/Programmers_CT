from collections import deque
def solution(n, edge):
    answer = 0
    edge_dict = {}
    length_saver = [999999999 for i in range(n+1)] # index 는 1부터, 0은 -1로
    length_saver[0] = 9999999
    for vertex in edge:
        if vertex[0] not in edge_dict:
            edge_dict[vertex[0]] = [vertex[1]]
        else:
            edge_dict[vertex[0]].append(vertex[1])
        if vertex[1] not in edge_dict:
            edge_dict[vertex[1]] = [vertex[0]]
        else:
            edge_dict[vertex[1]].append(vertex[0])
    que = deque([(1,1)])#num of node, value
    while que:
        node, value = que.popleft() 
        if length_saver[node] > value:
            length_saver[node] = value
            next_target = edge_dict[node]
            for i in next_target:
                que.append((i,value+1))
    target = max(length_saver[1:]) 
    for i in length_saver[1:]:
        if i == target:
            answer += 1
    return answer