import sys
from itertools import combinations
first = True
while True:
    input = sys.stdin.readline().strip().split()
    if input[0] == '0':
        break
    if not first:
        print()
    if first:
        first = False
    comb = list(combinations(input[1:], 6))
    for c in comb:
        print(' '.join(c))