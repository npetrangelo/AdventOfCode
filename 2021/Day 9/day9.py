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