filename = "input.txt"

num = 0
output_sum = 0

with open(filename) as f:
    for line in f:
        digits = [set() for _ in range(10)]
        segments, output = line.strip().split(" | ")
#         print(segments)
        for digit in output.split():
#             print(digit)
            if len(digit) in {2, 3, 4, 7}:
                num += 1
        
        digits[8] = set('abcdefg')
        corners = set('abcdefg')
        mid3 = set('abcdefg')
        for digit in segments.split():
            digit = set(digit)
            if len(digit) == 6:
                corners &= digit
            if len(digit) == 5:
                mid3 &= digit
            elif len(digit) == 4:
                digits[4] |= digit
            elif len(digit) == 3:
                digits[7] |= digit
            elif len(digit) == 2:
                digits[1] |= digit
#         top = digits[7] - digits[1]
        digits[3] = digits[1] | mid3
        digits[5] = corners | mid3
        digits[2] = (digits[8] - digits[5]) | mid3
        digits[0] = digits[8] - (digits[4] & mid3)
        digits[9] = digits[5] | digits[3]
        digits[6] = (digits[8] - digits[9]) | digits[5]
#         print(" ".join(["".join(digit) for digit in digits]))
        result = int("".join([str(digits.index(set(digit))) for digit in output.split()]))
#         print(result)
        output_sum += result

print(num, output_sum)
