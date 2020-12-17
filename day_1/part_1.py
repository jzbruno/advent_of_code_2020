#!/usr/bin/env python

data = []
with open('input') as f:
    data = f.readlines()
data = sorted(data)

for x in data:
    x = int(x.strip())
    for y in data[1:]:
        y = int(y.strip())
        if x + y == 2020:
            print(f'found {x} + {y} = 2020')
            print(f'{x * y}')
            exit(0)
