#! /usr/bin/env python3
import sys

with open("day4.txt", "r") as f:
    values = list(map(lambda line: line.strip(), f.readlines()))

# part 1
boards = []
draw_order = list(map(lambda num: int(num), values[0].split(',')))
values = list(filter(lambda line: line != '', values[1:]))
finished = False
winning_number = 0
winning_board = []
losing_number = 0
losing_board = []
found_losing_number = False
found_losing_board = False

for index in range(0, len(values), 5):
    board = {'winning': False}
    rows = list(filter(lambda line: line != '', ' '.join(values[index:index + 5]).split(' ')))
    board['rows'] = list(map(lambda t: {'number': int(t), 'picked': False}, rows))
    boards.append(board)

for draw_number in draw_order:
    # selecting number
    for board in boards:
        if board['winning'] is False:
            for number in board['rows']:
                if number['number'] == draw_number:
                    number['picked'] = True
                # determine if the board won
                # diagonal
                if (
                        board['rows'][0]['picked'] is True and
                        board['rows'][6]['picked'] is True and
                        board['rows'][12]['picked'] is True and
                        board['rows'][18]['picked'] is True and
                        board['rows'][24]['picked'] is True
                ):
                    board['winning'] = True
                    if finished is False:
                        finished = True
                        winning_number = draw_number
                        winning_board = board

                if (
                        board['rows'][4]['picked'] is True and
                        board['rows'][8]['picked'] is True and
                        board['rows'][12]['picked'] is True and
                        board['rows'][16]['picked'] is True and
                        board['rows'][20]['picked'] is True
                ):
                    board['winning'] = True
                    if finished is False:
                        finished = True
                        winning_number = draw_number
                        winning_board = board

                # horizontal
                for index in range(0, len(board['rows']), 5):
                    if (
                            board['rows'][index]['picked'] is True and
                            board['rows'][index + 1]['picked'] is True and
                            board['rows'][index + 2]['picked'] is True and
                            board['rows'][index + 3]['picked'] is True and
                            board['rows'][index + 4]['picked'] is True
                    ):
                        board['winning'] = True
                        if finished is False:
                            finished = True
                            winning_number = draw_number
                            winning_board = board

                # vertical
                for index in range(0, 5):
                    if (
                            board['rows'][index]['picked'] is True and
                            board['rows'][index + 5]['picked'] is True and
                            board['rows'][index + 10]['picked'] is True and
                            board['rows'][index + 15]['picked'] is True and
                            board['rows'][index + 20]['picked'] is True
                    ):
                        board['winning'] = True
                        if finished is False:
                            finished = True
                            winning_number = draw_number
                            winning_board = board

        losing_boards = list(filter(lambda q: q['winning'] is False, boards))
        if found_losing_board is False and len(losing_boards) == 1:
            losing_board = losing_boards[0]
            # print("losing board: ", losing_board)
            print('losing number: ', draw_number)
            found_losing_board = True
        if found_losing_number is False and len(losing_boards) == 0:
            losing_number = draw_number
            print('losing number 2: ', losing_number)
            # print("losing board 2: ", losing_board)
            found_losing_number = True

unmarked_numbers = list(filter(lambda num: num['picked'] is False, winning_board['rows']))
unmarked_numbers = sum(list(map(lambda x: x['number'], unmarked_numbers)))
unmarked_numbers_losing = list(filter(lambda num: num['picked'] is False, losing_board['rows']))
unmarked_numbers_losing = sum(list(map(lambda x: x['number'], unmarked_numbers_losing)))
print("part 1: ", unmarked_numbers * winning_number)
print("part 2: ", unmarked_numbers_losing * losing_number)
# too low - 1352
