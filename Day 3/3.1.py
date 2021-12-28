report = []
gamma_list = []
epsilon_list = []

with open('AoC-2021/Day 3/input3.txt') as f:
    for line in f:
        report.append(line.strip())

for i in range(0, len(report[0])):
    column = [x[i] for x in report] # Creates lists for each column of bits
    counter0 = 0 # Counters to compare the amounts of 0s and 1s in each column
    counter1 = 0
    for bit in column:
        if bit == '0':
            counter0 += 1
        elif bit == '1':
            counter1 += 1
    if counter0 > counter1: # Creates a list of most/least common bits for each column for gamma/epsilon rates respectively
        gamma_list.append(0)
        epsilon_list.append(1)
    else:
        gamma_list.append(1)
        epsilon_list.append(0)

gamma_rate = int("".join(map(str, gamma_list)), 2) # Converts the list of binary data to an integer 
epsilon_rate = int("".join(map(str, epsilon_list)), 2)

result = gamma_rate * epsilon_rate
print(result)