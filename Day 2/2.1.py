commands = []
forward = []
down = []
up = []

forward_values = []
down_values = []
up_values = []

forward_total = 0
down_total = 0
up_total = 0

with open('AoC-2021/Day 2/input2.txt') as f:
    for line in f:
        commands.append(line.strip())

for command in commands:
    if 'forward' in command:
        forward.append(command.split()) # Splits the word "forward" and value 
    if 'down' in command:
        down.append(command.split()) # Splits the word "down" and value 
    if 'up' in command:
        up.append(command.split()) # Splits the word "up" and value 

for command in forward:
    command.pop(0) # Removes the word "forward" leaving only the value
    forward_values.append(int(command[0])) # Converts values to int and appends them to a new list
for command in down:
    command.pop(0) # Removes the word "down" leaving only the value
    down_values.append(int(command[0]))
for command in up: 
    command.pop(0) # Removes the word "up" keaving only the value
    up_values.append(int(command[0]))

forward_total = sum(forward_values) # Adds all forward values
down_total = sum(down_values) # Adds all down values
up_total = sum(up_values) # Adds all up values

depth =  down_total - up_total # "up" values decrease the depth, so they are subtracted
result = forward_total * depth

print(result)