filename = "test2.txt"

tree = [None]*16

with open(filename) as f:
    line = f.readline().strip().strip('[]')
    for c in line:
        if c == ',':
            continue
        
    for line in f:
        n = line.strip().strip('[]')
        print(n)