x = 0
y = 1
measurements = []
counter = 0

with open('AoC-2021/Day 1/input1.txt') as f:
    for line in f:
        measurements.append(int(line.strip())) # Puts the input data in a list and removes newline characters

for i in range(0, (len(measurements) - 1)): # Iterates through list length - 1, so there are always 2 values to compare
    a = measurements[x] # a is initially the first value in the list
    b = measurements[y] # b is initially the second value in the list

    if b > a: # Checks if the measurement has increased from the previous measurement
        counter += 1
        x += 1 
        y += 1 # Increments x and y to compare the next pair of values
    else:
        x += 1
        y += 1

print(counter)