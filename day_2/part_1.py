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
    least, most, letter, password = parse(line)

    count = password.count(letter)
    if count >= least and count <= most:
        valid_count += 1

print(f'found {valid_count} valid passwords out of {len(data)}')
