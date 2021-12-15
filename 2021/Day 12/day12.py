filename = "input.txt"

caves = {}

with open(filename) as f:
    for line in f:
        start, end = line.strip().split("-")
        if start in caves:
            caves[start] |= {end}
        else:
            caves[start] = {end}
        
        if end in caves:
            caves[end] |= {start}
        else:
            caves[end] = {start}

# print(caves)

num_paths = 0

def travel1(cave, path):
    global num_paths
    if cave == "end":
        num_paths += 1
#         print(path)
        return
    for neighbor in caves[cave]:
        if neighbor.islower() and neighbor in path:
            continue
        if neighbor == "start":
            continue
        travel1(neighbor, path + [neighbor])

travel1("start", ["start"])
print(num_paths)