import sys

N, K = list(map(int,sys.stdin.readline().strip().split()))

upper = 1
lower = 1
for i in range(K+1, N+1):
    upper *= i
for i in range(1, N-K+1):
    lower *= i

print(int(upper // lower) % 10007 )