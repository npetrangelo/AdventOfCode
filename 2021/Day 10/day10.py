filename = "input.txt"

chunks = {'{':'}', '(':')', '<':'>', '[':']'}
scores = {')':3, ']':57, '}':1197, '>':25137}

score_list = []

def parse(line):
    stack = []
    for char in line:
        if char in chunks:
            stack.append(chunks[char])
            continue
        if char != stack.pop():
            return []
    return list(reversed(stack))

with open(filename) as f:
    for line in f:
#         print(line.strip())
        stack = []
        for char in line.strip():
            if char in chunks:
                stack.append(chunks[char])
                continue
            close = stack.pop()             
            if char != close:
#                 print(char, close)
                score_list.append(scores[char])
                break

# print(score_list)
print(sum(score_list))

scores = {')':1, ']':2, '}':3, '>':4}

stacks = []
score_list = []

with open(filename) as f:
    for line in f:
        stack = parse(line.strip())
        if len(stack) != 0:
            stacks.append(stack)
            total_score = 0
#             print(f"Start with a total score of {total_score}.")
            for c in stack:
#                 print(f"Multiply the total score by 5 to get {5*total_score}, then add the value of {c} ({scores[c]}) to get a new total score of {5*total_score+scores[c]}.")
                total_score = 5*total_score + scores[c]
            score_list.append(total_score)
            print("".join(stack), total_score)

print(f"Middle score: {sorted(score_list)[len(score_list)//2]}")
