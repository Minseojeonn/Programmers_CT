from collections import deque
def build_tree(node,edges):
    tree = [[] for _ in range(len(node))]
    for i in edges:
        parent, son = i[0], i[1]
        tree[parent].append(son)
    return tree

def solution(info, edges):
    #트리 구축
    max_sheep = -1
    tree = build_tree(info,edges)
    que = deque()
    que.append((0,1,0,set()))#다음타겟, 해당위치 양수, 해당위치늑대수
    while que:
        candidate = que.popleft()
        current, c_sheep, c_wolf, next_node = candidate[0], candidate[1], candidate[2], candidate[3]
        next_node.update(tree[current])    
        max_sheep = max(c_sheep,max_sheep)
        for i in next_node:
            if info[i] == 0: #sheep
                que.append((i,c_sheep+1,c_wolf,next_node-{i}))
            else:#wolf
                if c_sheep > c_wolf+1:
                    que.append((i,c_sheep,c_wolf+1,next_node-{i}))
    answer = max_sheep
    return answer


'''
#트리 구축
#트리 순환
#최대 양 수 반환
#조건 추가
'''