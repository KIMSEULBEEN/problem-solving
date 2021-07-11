import sys

data = sys.stdin.read()
trees = data.split('\n')

len_trees = 0
trees_dict = {}
for tree_name in trees:
    if tree_name != '':
        len_trees += 1
        if tree_name in trees_dict.keys():
            trees_dict[tree_name] += 1
        else:
            trees_dict[tree_name] = 1

trees_dict = dict(sorted(trees_dict.items()))

for tree in trees_dict.keys():
    print("%s %.4f" % (tree, trees_dict[tree] * 100 / len_trees))
