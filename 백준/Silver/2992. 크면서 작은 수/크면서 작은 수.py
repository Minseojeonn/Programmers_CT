import sys
from itertools import permutations

in_int = int(sys.stdin.readline().strip())
smallest = float('inf')
for candidate in permutations(str(in_int), len(str(in_int))):
    int_candidate = int("".join(candidate))
    if int_candidate > in_int and int_candidate != in_int:
        smallest = min(smallest, int_candidate)
        
if smallest == float("inf"):
    print(0)
else:
    print(smallest)