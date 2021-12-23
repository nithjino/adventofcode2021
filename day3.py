#! /usr/bin/env python3
import copy

with open("day3.txt", "r") as f:
    values = list(map(lambda y: y.strip(), f.readlines()))

# part 1
gamma_rate = ''
epsilon_rate = ''

for index in range(len(values[0])):
    num_of_ones = len(list(filter(lambda x: x[index] == '1', values)))
    num_of_zeroes = len(list(filter(lambda x: x[index] == '0', values)))

    if num_of_ones > num_of_zeroes:
        gamma_rate = gamma_rate + '1'
        epsilon_rate = epsilon_rate + '0'
    else:
        gamma_rate = gamma_rate + '0'
        epsilon_rate = epsilon_rate + '1'

print("part 1: ", int(gamma_rate, 2) * int(epsilon_rate, 2))

# part 2
oxygen_generator_rating = ''
co2_scrubber_rating = ''
oxygen_numbers = copy.deepcopy(values)
co2_numbers = copy.deepcopy(values)

for index in range(len(values[0])):
    num_of_ones_oxygen = len(list(filter(lambda x: x[index] == '1', oxygen_numbers)))
    num_of_zeroes_oxygen = len(list(filter(lambda x: x[index] == '0', oxygen_numbers)))

    num_of_ones_co2 = len(list(filter(lambda x: x[index] == '1', co2_numbers)))
    num_of_zeroes_co2 = len(list(filter(lambda x: x[index] == '0', co2_numbers)))

    if len(oxygen_numbers) > 1:
        if num_of_zeroes_oxygen > num_of_ones_oxygen:
            oxygen_numbers = list(filter(lambda x: x[index] == '0', oxygen_numbers))
        else:
            oxygen_numbers = list(filter(lambda x: x[index] == '1', oxygen_numbers))

    if len(co2_numbers) > 1:
        if num_of_zeroes_co2 > num_of_ones_co2:
            co2_numbers = list(filter(lambda x: x[index] == '1', co2_numbers))
        else:
            co2_numbers = list(filter(lambda x: x[index] == '0', co2_numbers))

print("part 2: ", int(oxygen_numbers[0], 2) * int(co2_numbers[0], 2))
