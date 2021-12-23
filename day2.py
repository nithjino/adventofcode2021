#! /usr/bin/env python3

with open("day2.txt", "r") as f:
    values = list(map(lambda z: [z[0].strip(), int(z[1])], list(map(lambda y: y.strip().split(' '), f.readlines()))))

# part 1
depth = 0
horizontal = 0

for value in values:
    direction, x = value
    match direction:
        case 'forward':
            horizontal = horizontal + x
        case 'down':
            depth = depth + x
        case 'up':
            depth = depth - x
        case _:
            pass

print("part 1: ", depth * horizontal)

# part 2
depth = 0
horizontal = 0
aim = 0

for value in values:
    direction, x = value
    match direction:
        case 'forward':
            horizontal = horizontal + x
            depth = depth + (aim * x)
        case 'down':
            aim = aim + x
        case 'up':
            aim = aim - x
        case _:
            pass

print("part 2: ", depth * horizontal)
