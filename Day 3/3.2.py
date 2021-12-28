from copy import copy

report = []

with open('AoC-2021/Day 3/input3.txt') as f:
    for line in f:
        report.append(line.strip())

oxygen_generator, CO2_scrubber = copy(report), copy(report)

def common0_oxygen(bit, position=0): # Functions to determine if a bit in a column is equal to the most or least
    if bit[position] == '0':         # common bit for each column, logic is reversed for CO2 functions
        return True
    else:
        return False

def common0_CO2(bit, position=0):
    if bit[position] != '0':
        return True
    else:
        return False

def common1_oxygen(bit, position=0):
    if bit[position] == '1':
        return True
    else:
        return False

def common1_CO2(bit, position=0):
    if bit[position] != '1':
        return True
    else:
        return False

for i in range(0, len(oxygen_generator[0])): 
    column = [x[i] for x in oxygen_generator]
    counter0 = 0
    counter1 = 0
    for bit in column:
        if bit == '0':
            counter0 += 1
        elif bit == '1':
            counter1 += 1
    if counter0 > counter1: # Removes values that do not contain the most common bit from the list
        oxygen_generator = list(filter(lambda bit: common0_oxygen(bit, position=i), oxygen_generator))
    elif counter1 > counter0:
        oxygen_generator = list(filter(lambda bit: common1_oxygen(bit, position=i), oxygen_generator))
    elif counter1 == counter0:
        oxygen_generator = list(filter(lambda bit: common1_oxygen(bit, position=i), oxygen_generator))

for i in range(0, len(CO2_scrubber[0])):
    column = [x[i] for x in CO2_scrubber]
    counter0 = 0
    counter1 = 0
    for bit in column:
        if bit == '0':
            counter0 += 1
        elif bit == '1':
            counter1 += 1
    if len(CO2_scrubber) == 1: # Stops once there is only 1 value left in the list
        break
    if counter0 > counter1: # Removes values that do not contain the least common bit from the list
        CO2_scrubber = list(filter(lambda bit: common0_CO2(bit, position=i), CO2_scrubber))
    elif counter1 > counter0:
        CO2_scrubber = list(filter(lambda bit: common1_CO2(bit, position=i), CO2_scrubber))
    elif counter1 == counter0:
        CO2_scrubber = list(filter(lambda bit: common1_CO2(bit, position=i), CO2_scrubber))
 
oxygen_rating = int("".join(map(str, oxygen_generator)), 2) # Converts each list of binary values to an integer
CO2_rating = int("".join(map(str, CO2_scrubber)), 2)

result = oxygen_rating * CO2_rating
print(result)