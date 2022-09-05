input = []
called_numbers = []

with open('Day 4/input4.txt') as f: 
    for line in f:
        input.append(line.strip())

called = input[0].replace(',', ' ') # Store the first line of numbers

for number in called.split():
    called_numbers.append(int(number))

del input[0:2] # Remove the called numbers and empty line after it to make iterating through boards easier

card = []

complete = ['*', '*', '*', '*', '*']

counts = []
scores = []

def fill():
    for line in range(5):
        card.append(str(input[line]).split())

def empty():
    card.clear()
        
def onCard(card, number):
    for i in range(5):
        for j in range(5):
            if card[i][j] == number:
                card[i][j] = '*'

def isRow(card):
    for i in range(5):
        if card[i] == complete:
            return True

def isCol(card):
    column = []
    for j in range(5):
        for i in range(5):
            column.append(card[i][j])
        if column == complete:
            return True
        else:
            column = []
            continue

def findScore(card, last_num):
    sum = 0
    for i in range(5):
        for j in range(5):
            if card[i][j] != '*':
                sum += card[i][j]
    score = sum * last_num
    return score

# Testing setup

fill()
# print(card)
# print(called_numbers)

def bingo():
    turn_count = 0
    for number in called_numbers:
        onCard(card, number)
        isRow(card)
        isCol(card)
        turn_count += 1

        if isRow(card) or isCol(card):
            winning_number = number
            #print(winning_number)
            counts.append(turn_count)
            scores.append(findScore(card, winning_number))

# Have to find a way to repeat this for each card given in the input file

card_count = 1 # Start at 1 to account for the last card

for line in input:
    if line == '':
        card_count += 1

for i in range(card_count):
    fill()
    bingo()
    empty()
    del input[0:6] # Remove the card to check the new one

print(counts)
print(scores)