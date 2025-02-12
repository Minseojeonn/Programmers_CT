import sys
from collections import defaultdict
from collections import deque

num_edges = int(sys.stdin.readline().strip())
edge_checker = {}
edge_dict = defaultdict(list)

for i in range(num_edges-1):
    edge_checker[i] = False
    fr, to = sys.stdin.readline().strip().split()
    edge_dict[fr].append((to, i))
    edge_dict[to].append((fr, i))

queue = deque(['1'])
tree = {}
while queue:
    next = queue.popleft() 
    for candidate in edge_dict[next]:
        if edge_checker[candidate[1]] == False:
            edge_checker[candidate[1]] = True
            queue.append(candidate[0])
            tree[candidate[0]] = next
for i in range(2, num_edges+1):
    print(tree[str(i)])