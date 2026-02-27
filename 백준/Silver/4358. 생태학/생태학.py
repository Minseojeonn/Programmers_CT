import sys
tree_dict = {}
num_trees = 0

for line in sys.stdin:
    tree_type = line.strip()
    if tree_type in tree_dict:
        tree_dict[tree_type] += 1
    else:
        tree_dict[tree_type] = 1
    num_trees += 1

if len(tree_dict.keys()) > 0:
    for ttype in sorted(tree_dict.keys()):
        precentile = (tree_dict[ttype] / num_trees) * 100
        print(f"{ttype} {precentile:.4f}")


