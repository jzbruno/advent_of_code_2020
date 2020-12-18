#!/usr/bin/env python

lines = []
with open('input') as f:
    lines = f.readlines()

tree_count = 0
cell = 3
for line in lines[1:]:
    line = line.strip()
    cell = cell % len(line)
    if line[cell] == '#':
        tree_count += 1

    cell += 3

print(f'found {tree_count} trees')
