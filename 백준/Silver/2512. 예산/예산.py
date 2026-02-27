num_country = int(input())
request = list(map(int, input().split(" ")))
request.sort()
budget = int(input())

start = 1
end = request[-1]

while start <= end:
    mid = (start + end) // 2
    remain = budget
    for req in request:
        if req <= mid:
            remain -= req
        else:
            remain -= mid
    
    if remain >= 0:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)