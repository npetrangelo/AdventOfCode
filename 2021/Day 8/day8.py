filename = "input.txt"

num = 0

with open(filename) as f:
    for line in f:
        segments, output = line.strip().split(" | ")
#         print(output)
        for digit in output.split():
            if len(digit) in {2, 3, 4, 7}:
                num += 1

print(num)
