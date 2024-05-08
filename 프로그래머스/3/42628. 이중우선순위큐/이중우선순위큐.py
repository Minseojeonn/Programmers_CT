def solution(operations):
    lit = []
    for i in operations:
        operation, value = i.split(" ")
        value = int(value)
        if operation == 'I':
            lit.append(value)
            lit = sorted(lit)
        if operation == "D":
            if value == -1 and len(lit)>0:
                del lit[0]
            if value == 1 and len(lit)>0:
                del lit[-1]
    if len(lit) == 0:
        answer = [0,0]
    else:
        answer = [lit[-1],lit[0]]
    return answer