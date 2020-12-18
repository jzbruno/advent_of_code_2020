#!/usr/bin/env python

import re

data = []
with open('input') as f:
    data = f.read().strip()

raw_records = data.split('\n\n')
valid_count = 0

for raw_record in raw_records:
    raw_fields = re.split('\n| ', raw_record)
    record = {}
    for raw_field in raw_fields:
        k, v = raw_field.split(':')
        record[k] = v
    if all(k in record for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')):
        valid_count += 1

print(valid_count)
