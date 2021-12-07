import math

filename = "input.txt"

sea_map = [[0,]*1000 for i in range(1000)]

def print_map(sea_map):
    for row in sea_map:
        print("".join(["." if char == "0" else char for char in [str(num) for num in row]]))
        
# print_map(sea_map)

with open(filename) as f:
    for line in f:
        vent = [[int(num) for num in pair.split(",")] for pair in line.strip().split(" -> ")]
        if vent[0][1] == vent[1][1]:
            min_i = min(vent[0][0], vent[1][0])
            max_i = max(vent[0][0], vent[1][0])
            for i in range(min_i, max_i+1):
                sea_map[vent[0][1]][i] += 1
        if vent[0][0] == vent[1][0]:
            min_i = min(vent[0][1], vent[1][1])
            max_i = max(vent[0][1], vent[1][1])
            for i in range(min_i, max_i+1):
                sea_map[i][vent[0][0]] += 1
        if abs(vent[0][0]-vent[1][0]) == abs(vent[0][1]-vent[1][1]):
#             print(vent)
#             print(abs(vent[0][0]-vent[1][0]), abs(vent[0][1]-vent[1][1]))
            x_step = int(math.copysign(1, vent[1][0]-vent[0][0]))
            y_step = int(math.copysign(1, vent[1][1]-vent[0][1]))
#             print(x_step, y_step)
            x_list = list(range(vent[0][0], vent[1][0]+x_step, x_step))
            y_list = list(range(vent[0][1], vent[1][1]+y_step, y_step))
#             print(x_list, y_list)
            for x,y in zip(x_list, y_list):
                sea_map[y][x] += 1
            

# print_map(sea_map)

num_plural = 0
for row in sea_map:
    for num in row:
        if num >= 2:
            num_plural += 1

print(f"num_plural={num_plural}")