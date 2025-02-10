import sys

num_tree, togo = list(map(int, sys.stdin.readline().strip().split()))
tree = list(map(int, sys.stdin.readline().strip().split()))
tree = sorted(tree, reverse=True)
tree.append(0)
taken = 0
skip_tree = 0
saved = 0
while taken < num_tree:
    diff = (tree[taken] - tree[taken+1]) * (taken+1)
    if diff + saved >= togo:
        #print(f"{taken}, {saved}, input")
        pivot = 0
        while True:
            #print(pivot)
            if saved + (taken+1) * pivot >= togo:
                print(tree[taken] - pivot)
                exit()
            else:
                pivot += 1
    else:
        saved += diff
    taken += 1
