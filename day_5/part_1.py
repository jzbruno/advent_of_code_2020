#!/usr/bin/env python

import sys
from math import ceil, floor


def get_boarding_passes(filename):
    boarding_passes = []
    with open(filename) as f:
        boarding_passes = f.readlines()

    return boarding_passes


def get_row(row_letters):
    rows = [*range(128)]

    for row_letter in row_letters:
        if row_letter == 'B':  # upper
            rows = rows[ceil(len(rows) / 2):]
        if row_letter == 'F':  # lower
            rows = rows[:floor(len(rows) / 2)]

    return rows[0]


def get_col(col_letters):
    cols = [*range(8)]

    for col_letter in col_letters:
        if col_letter == 'R':  # upper
            cols = cols[ceil(len(cols) / 2):]
        if col_letter == 'L':  # lower
            cols = cols[:floor(len(cols) / 2)]

    return cols[0]


def parse_seats(filename):
    seats = []
    for boarding_pass in get_boarding_passes(filename):
        boarding_pass = boarding_pass.strip()

        row = get_row(boarding_pass[:7])
        col = get_col(boarding_pass[-4:])

        seats.append({
            'boarding_pass': boarding_pass,
            'row': get_row(boarding_pass[:7]),
            'col': get_col(boarding_pass[-4:]),
            'seat_id': (row * 8) + col,
        })

    return seats


if __name__ == '__main__':
    if len(sys.argv) == 1:
        filename = 'input'
    else:
        filename = sys.argv[1]

    seats = parse_seats(filename)
    seats = sorted(seats, key=lambda s: s['seat_id'])

    for seat in seats:
        print(f"{seat['boarding_pass']}: row {seat['row']}, column {seat['col']}, seat ID {seat['seat_id']}.")
