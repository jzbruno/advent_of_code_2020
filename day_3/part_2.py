#!/usr/bin/env python

lines = []
with open('input') as f:
    lines = f.readlines()

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]
tree_count_prod = 1

for slope in slopes:
    x, y = slope
    cell = x
    tree_count = 0

    for i in range(y, len(lines), y):
        line = lines[i].strip()
        cell = cell % len(line)
        if line[cell] == '#':
            tree_count += 1
        cell += x

    print(f'found {tree_count} trees')
    tree_count_prod = tree_count_prod * tree_count

print(f'found {tree_count_prod} total trees')
