a1 = 0 # Starting indexes for each 3 measurement group
a2 = 1
a3 = 2
b1 = 1
b2 = 2
b3 = 3
measurements = []
counter = 0

with open('AoC-2021/Day 1/input1.txt') as f:
    for line in f:
        measurements.append(int(line.strip())) # Puts the input data in a list and removes newline characters

for i in range(0, (len(measurements) - 3)): # Iterates through list length - 3, so there are always 2 values to compare
    a = measurements[a1] + measurements[a2] + measurements[a3] # Adds the 3 measurements for each group
    b = measurements[b1] + measurements[b2] + measurements[b3] 

    if b > a: # Checks if the measurement has increased from the previous measurement
        counter += 1
        a1 += 1 # Increments a and b to compare the next pair of measurements
        a2 += 1
        a3 += 1
        b1 += 1
        b2 += 1
        b3 += 1
    else:
        a1 += 1 
        a2 += 1
        a3 += 1
        b1 += 1
        b2 += 1
        b3 += 1

print(counter)