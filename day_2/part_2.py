#!/usr/bin/env python

data = []
with open('input') as f:
    data = f.readlines()


def parse(line):
    policy, password = line.strip().split(':')
    limits, letter = policy.strip().split(' ')
    least, most = limits.strip().split('-')

    return int(least), int(most), letter, password.strip()


valid_count = 0
for line in data:
    pos_1, pos_2, letter, password = parse(line)

    matches = 0
    if password[pos_1-1] == letter:
        matches += 1
    if password[pos_2-1] == letter:
        matches += 1

    if matches == 1:
        valid_count += 1

print(f'found {valid_count} valid passwords out of {len(data)}')
