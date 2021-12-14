import sys
from termcolor import colored, cprint

filename = "input.txt"

octopuses = []
num_flashed = 0
flashed = set()

with open(filename) as f:
    for line in f:
        octopuses.append([int(c) for c in line.strip()])

def color(c):
#     if c == 9:
#         return colored(str(c), 'green')
    return colored(str(c), 'blue') if c != 0 else str(c)

def print_octos(octos):
    print()
    for row in octos:
        print("".join([color(c) for c in row]))
        
def flash(x, y):
    global flashed, num_flashed
    if not -1 < y < len(octopuses) or not -1 < x < len(octopuses[0]):
        return
    if (x,y) in flashed:
        return
    octopuses[y][x] += 1
    if not octopuses[y][x] > 9:
        return
    octopuses[y][x] = 0
    flashed |= {(x,y)}
    num_flashed += 1
    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            flash(i, j)

def step():
    global flashed
    flashed = set()
    for y in range(len(octopuses)):
        for x in range(len(octopuses[0])):
            flash(x, y)

for _ in range(100):
    step()

print(num_flashed)
