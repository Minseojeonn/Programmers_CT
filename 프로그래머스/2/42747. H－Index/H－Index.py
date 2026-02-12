def solution(citations):
    answer = 0
    sorted_citations = sorted(citations)[::-1]
    for pivot in range(max(citations)):
        num_over_pivot = 0
        for citation in sorted_citations:
            if citation >= pivot:
                num_over_pivot += 1
            else:
                break
        if num_over_pivot >= pivot:
            answer = max(answer, pivot)
    return answer
#논문 편중, h번 이상 인용된 논문이 h편 이상일때, H_index = h

