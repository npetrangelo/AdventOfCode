import math

filename = "input.txt"

heightmap = []

with open(filename) as f:
    for line in f:
#         print(line.strip())
        heightmap.append([int(char) for char in line.strip()])

risk = 0

for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        this = heightmap[y][x]
        left = heightmap[y][x-1] if x > 0 else 0xFFFFFFF
        right = heightmap[y][x+1] if x < len(heightmap[0])-1 else 0xFFFFFFF
        above = heightmap[y-1][x] if y > 0 else 0xFFFFFFF
        below = heightmap[y+1][x] if y < len(heightmap)-1 else 0xFFFFFFF
#         print(x,y, heightmap[y][-1])
        if this < right and this < below and this < left and this < above:
#             print(this)
            risk += this+1

print(risk)

basins = []

for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        if heightmap[y][x] == 9:
            continue
        left_basin = list(filter(lambda basin: (x-1,y) in basin, basins))
        above_basin = list(filter(lambda basin: (x,y-1) in basin, basins))
        left_basin = left_basin[0] if len(left_basin) == 1 else set()
        above_basin = above_basin[0] if len(above_basin) == 1 else set()
        basin = {(x,y)} | left_basin | above_basin
        if left_basin in basins:
            basins.remove(left_basin)
        if above_basin in basins:
            basins.remove(above_basin)
        basins.append(basin)

sizes = sorted([len(basin) for basin in basins])

print(math.prod(sizes[-3:]))