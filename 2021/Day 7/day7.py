import math

filename = "input.txt"

def calc_fuel(crabs, pos):
    return sum([abs(crab-pos) for crab in crabs])
    
def calc_fuel_gauss(crabs, pos):
    return sum([abs(crab-pos)*(abs(crab-pos)+1)/2 for crab in crabs]) 

def min_fuel(crabs):
    prev = 0xFFFFFFFF
    for pos in range(min(crabs), max(crabs)+1):
        fuel = calc_fuel_gauss(crabs, pos)
        if fuel > prev:
            return prev, pos-1
        prev = fuel

with open(filename) as f:
    crabs = [int(pos) for pos in f.readline().strip().split(",")]
#     print(crabs)
    fuel, min_pos = min_fuel(crabs)
    print(f"Position {min_pos} with {fuel} fuel burned")