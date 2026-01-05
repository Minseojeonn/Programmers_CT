def solution(edges):
    # 각 노드별 들어오는/나가는 간선 수 기록
    # 노드 번호가 최대 1,000,000까지 가능하므로 딕셔너리가 효율적입니다.
    in_degree = {}
    out_degree = {}
    nodes = set()

    for fr, to in edges:
        out_degree[fr] = out_degree.get(fr, 0) + 1
        in_degree[to] = in_degree.get(to, 0) + 1
        nodes.add(fr)
        nodes.add(to)

    hub_node = -1
    donut, bar, eight = 0, 0, 0

    for node in nodes:
        out_cnt = out_degree.get(node, 0)
        in_cnt = in_degree.get(node, 0)

        # 1. 생성된 정점 찾기: 들어오는 것 0, 나가는 것 2개 이상
        if in_cnt == 0 and out_cnt >= 2:
            hub_node = node
        
        # 2. 막대 그래프 찾기: 나가는 간선이 0개인 노드가 반드시 1개 존재
        # (생성된 정점은 제외해야 하지만, 생성된 정점은 위에서 out_cnt >= 2로 걸러짐)
        elif out_cnt == 0:
            bar += 1
            
        # 3. 8자형 그래프 찾기: 나가는 간선이 2개인 노드가 반드시 1개 존재
        # (생성된 정점에서 오는 간선 때문에 in_degree는 2 이상이 됨)
        elif out_cnt == 2:
            eight += 1

    # 4. 도넛 그래프 계산
    # 전체 그래프 개수 = 생성된 정점에서 나가는 간선의 총 개수
    total_graphs = out_degree[hub_node]
    donut = total_graphs - bar - eight

    return [hub_node, donut, bar, eight]