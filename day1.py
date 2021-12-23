#! /usr/bin/env python3

with open("day1.txt", "r") as f:
    values = list(map(lambda y: int(y.strip()), f.readlines()))

# part 1
x = values[0]
counter = 0
for index in range(1, len(values)):
    value = values[index]
    if value > x:
        counter = counter + 1
    x = value
print("part 1: ", counter)

# part 2
counter = 0
x = values[0] + values[1] + values[2]

for index in range(len(values) - 2):
    sum = values[index] + values[index + 1] + values[index + 2]
    if sum > x:
        counter = counter + 1
    x = sum
print("part 2: ", counter)

