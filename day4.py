#! /usr/bin/env python3
import sys

with open("day4.txt", "r") as f:
    values = list(map(lambda line: line.strip(), f.readlines()))

# part 1
boards = []
draw_order = list(map(lambda num: int(num), values[0].split(',')))
values = list(filter(lambda line: line != '', values[1:]))
winning_indices = []
for index in range(0, len(values), 5):
    board = {'winning': False, 'rows': []}
    for increment in range(5):
        row = list(filter(lambda line: line != '', values[index + increment].split(' ')))
        row = list(map(lambda t: {'number': int(t), 'picked': False}, row))
        board['rows'].append(row)
    boards.append(board)

'''
for draw_number in draw_order:
    # selecting number
    for board in boards:
        for row in board['rows']:
            for number in row:
                if number['number'] == draw_number:
                    number['picked'] = True
        # determine if the board won
    # check if any board are marked as winnable
    winning_boards = list(filter(lambda b: b['winning'] is True, boards))
'''