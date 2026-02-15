A = map(int, input().split())
sum = 0
for i in A:
    sum += i**2
print(sum % 10)