#!/usr/bin/env python

import inspect
import json
import re
import sys


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
def is_valid_byr(val):
    fn = f'{inspect.stack()[0][3]}({val})'

    if len(val) != 4:
        print(f'failed {fn}: not 4 digits')
        return False

    try:
        val = int(val)
    except:
        print(f'failed {fn}: not a number')
        return False

    if 1920 <= val <= 2002:
        return True

    print(f'failed {fn}: 1920 <= {val} <= 2002')
    return False


# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
def is_valid_iyr(val):
    fn = f'{inspect.stack()[0][3]}({val})'

    if len(val) != 4:
        print(f'failed {fn}: not 4 digits')
        return False

    try:
        val = int(val)
    except:
        print(f'failed {fn}: not a number')
        return False

    if 2010 <= val <= 2020:
        return True

    print(f'failed {fn}: 2010 <= {val} <= 2020')
    return False


# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def is_valid_eyr(val):
    fn = f'{inspect.stack()[0][3]}({val})'

    if len(val) != 4:
        print(f'failed {fn}: not 4 digits')
        return False

    try:
        val = int(val)
    except:
        print(f'failed {fn}: not a number')
        return False

    if 2020 <= val <= 2030:
        return True

    print(f'failed {fn}: 2020 <= {val} <= 2030')
    return False


# hgt (Height) - a number followed by either cm or in:
#
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
#
def is_valid_hgt(val):
    fn = f'{inspect.stack()[0][3]}({val})'

    unit = val[-2:]
    if unit not in ['cm', 'in']:
        print(f'failed {fn}: must end with "cm" or "in", found {unit}')
        return False

    try:
        val = int(val[:-2])
    except:
        print(f'failed {fn}: not a number')
        return False

    if unit == 'cm':
        if 150 <= val <= 193:
            return True
        else:
            print(f'failed {fn}: cm 150 <= {val} <= 193')
            return False
    if unit == 'in':
        if 59 <= val <= 76:
            return True
        else:
            print(f'failed {fn}: in 59 <= {val} <= 76')
            return False

    print(f'failed {fn}: unknown reason')
    return False


# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def is_valid_hcl(val):
    fn = f'{inspect.stack()[0][3]}({val})'

    if re.match('#[a-fA-F0-9]{6}', val):
        return True
    else:
        print(f'failed {fn}: does not match regex #[a-f0-9]{{6}}')
        return False


# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def is_valid_ecl(val):
    fn = f'{inspect.stack()[0][3]}({val})'
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if val in colors:
        return True
    else:
        print(f'failed {fn}: not one of {colors}')
        return False


# pid (Passport ID) - a nine-digit number, including leading zeroes.
def is_valid_pid(val):
    fn = f'{inspect.stack()[0][3]}({val})'

    if re.match('[0-9]{9}', val):
        return True
    else:
        print(f'failed {fn}: does not match regex [0-9]{{9}}')
        return False


def has_fields(record):
    fn = f'{inspect.stack()[0][3]}({record})'
    expected_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    if 'cid' not in record:
        print('warning missing "cid" field')

    if expected_fields.issubset(record.keys()):
        return True

    print(f'failed {fn}: record is missing fields {expected_fields - record.keys()}')
    return False


def is_valid(record):
    return has_fields(record) and all([
        is_valid_byr(record['byr']),
        is_valid_ecl(record['ecl']),
        is_valid_eyr(record['eyr']),
        is_valid_hcl(record['hcl']),
        is_valid_hgt(record['hgt']),
        is_valid_iyr(record['iyr']),
        is_valid_pid(record['pid']),
    ])


if len(sys.argv) == 1:
    input_file = 'input'
else:
    input_file = sys.argv[1]

data = []
with open(input_file) as f:
    data = f.read().strip()

raw_records = data.split('\n\n')
records = []
valid_count = 0

for raw_record in raw_records:
    raw_fields = re.split('\n| ', raw_record)

    record = {}
    for raw_field in raw_fields:
        k, v = raw_field.split(':')
        record[k] = v
    records.append(record)

    if is_valid(record):
        print('valid record')
        valid_count += 1
    else:
        print('invalid record')

    print(json.dumps(record, indent=4))
    print()

print(f'found {valid_count} valid records of {len(records)}')
