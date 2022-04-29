filename = "input.txt"

dots = set()
folds = []

with open(filename) as f:
    for line in f:
        if line == "\n":
            break
#         print(f"Loop 1: {line.strip()}")
        dot = tuple([int(c) for c in line.strip().split(",")])
        
        dots.add(dot)
    for line in f:
        words = line.strip().split(" ")
        fold = words[2].split("=")
        fold[1] = int(fold[1])
        folds.append(fold)
#         print(f"Loop 2: {line.strip()}")

# print(dots)
# print(folds)

def reflect(dots, fold):
    new_dots = set()
    for dot in dots:
        if fold[0] == "x":
            new_dots.add((dot[0]-fold[1] if dot[0] > fold[1] else fold[1] - dot[0], dot[1]))
        if fold[0] == "y":
            new_dots.add((dot[0], dot[1] if dot[1] < fold[1] else 2*fold[1] - dot[1]))
    return new_dots

def print_paper(dots):
    min_x = min([dot[0] for dot in dots])
    min_y = min([dot[1] for dot in dots])
    size_x = max([dot[0] for dot in dots])-min_x+1
    size_y = max([dot[1] for dot in dots])-min_y+1
    paper = [[".",]*size_x for _ in range(size_y)]
    for dot in dots:
        x = dot[0]-min_x
        y = dot[1]-min_y
        paper[y][x] = "#"
    for row in paper:
        print("".join(row))
    print()

for fold in folds:
    dots = reflect(dots, fold)
print_paper(dots)
