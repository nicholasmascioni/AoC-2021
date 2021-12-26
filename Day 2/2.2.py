commands = []
horizontal = 0
aim = 0
depth = 0

with open('AoC-2021/Day 2/input2.txt') as f:
    for line in f:
        command, value = line.strip().split() # Creates a tuple to store the command and its value
        commands.append((command, int(value))) # Stores the tuples in the commands list

for element in commands:
    command = element[0]
    value = element[1]
    if command == 'down':
        aim += value            # Down increases the aim
    elif command == 'up':
        aim -= value            # Up decreases the aim
    elif command == 'forward':
        horizontal += value     # Forward increases the horizontal value
        depth += (aim * value)  # and increases the depth by the aim multiplied by its value
    print(aim)

result = horizontal * depth
print(result) 