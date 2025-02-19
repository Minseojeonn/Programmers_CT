import sys
import copy

H = int(sys.stdin.readline().strip())

tri = []
drow = [1, 1]
dcol = [0, 1]
for i in range(H):
    tri.append(list(map(int, sys.stdin.readline().split()))) 
tri_save = copy.deepcopy(tri)

for rowidx in range(H-1):
    candidate = tri[rowidx]
    for colidx, value in enumerate(candidate):
        for dr, dc in zip(drow, dcol):
            tri[rowidx+dr][colidx+dc] = max(tri[rowidx+dr][colidx+dc], tri_save[rowidx+dr][colidx+dc] + tri[rowidx][colidx])

print(max(tri[-1]))
#indexing은 양쪽다 -1임
#항상 성립하기때문에, 예외처리 X
