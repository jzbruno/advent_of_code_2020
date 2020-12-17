#!/usr/bin/env python

data = []
with open('input') as f:
    data = f.readlines()
data = sorted(data)

for x in data:
    x = int(x.strip())
    for y in data:
        y = int(y.strip())
        for z in data:
            z = int(z.strip())
            if x + y + z == 2020:
                print(f'found {x} + {y} + {z} = 2020')
                print(f'{x * y * z}')
                exit(0)
