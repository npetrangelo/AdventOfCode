filename = "input.txt"

chunks = {'{':'}', '(':')', '<':'>', '[':']'}
scores = {')':3, ']':57, '}':1197, '>':25137}

score_list = []

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