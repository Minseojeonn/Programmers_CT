import sys

#init point
num_nodes = int(sys.stdin.readline())
num_edges = int(sys.stdin.readline())

#build edgedict    
#bi-direct setting.
edge_dict = {}
for i in range(num_nodes+1):
    edge_dict[i] = []
for i in range(num_edges):
    src, dst = map(int, sys.stdin.readline().split())
    edge_dict[src].append(dst)
    edge_dict[dst].append(src)

#not duplicated visited
visited_dict = {}
have_to_visit = [1]

while have_to_visit:
    next = have_to_visit.pop()
    if next not in visited_dict:
        visited_dict[next] = True
        for connected in edge_dict[next]:    
            have_to_visit.append(connected)
        
#exclude node 1
print(len(visited_dict)-1)
    