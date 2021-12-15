from collections import Counter

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
        if neighbor == "start":
            continue
        if neighbor.islower() and neighbor in path:
            continue
        travel1(neighbor, path + [neighbor])

travel1("start", ["start"])
print(num_paths)

def small_cave_visted_twice(path):
    special = {"start", "end"}
    small_caves = list(filter(lambda c: c.islower() and c not in special, path))
    if not small_caves:
        return False
    c = Counter(small_caves)
#     print(c)
    cave, frequency = c.most_common(1)[0]
    return frequency > 1

num_paths = 0

def travel2(cave, path):
    global num_paths
    if cave == "end":
        num_paths += 1
#         print(path)
        return
    for neighbor in caves[cave]:
        if neighbor == "start":
            continue
        if neighbor.islower() and neighbor in path and small_cave_visted_twice(path):
#             print(path + [neighbor])
            continue
        travel2(neighbor, path + [neighbor])

travel2("start", ["start"])
print(num_paths)
