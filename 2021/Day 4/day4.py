def read_input(filename):
    file_lines = []
    with open(filename) as f:
        draws = [int(draw) for draw in f.readline().strip().split(",")]
        print(draws)
        
        lines = [line.strip() for line in f.readlines()]
        print()
        boards = []
        for i in range(1, len(lines), 6):
            board = [[int(x) for x in line.split()] for line in lines[i:i+5]]
            boards.append(board)
        
        for board in boards:
            print(board)
        
    return draws, boards

def won(board, drawn):
    for row in board:
        if drawn[row[0]] and drawn[row[1]] and drawn[row[2]] and drawn[row[3]] and drawn[row[4]]:
            return True
    
    for i in range(5):
        if drawn[board[0][i]] and drawn[board[1][i]] and drawn[board[2][i]] and drawn[board[3][i]] and drawn[board[4][i]]:
            return True
    
    return False

def winner():
    drawn = [False]*(max(draws)+1)
    for draw in draws:
        drawn[draw] = True
        for board in boards:
            if won(board, drawn):
                return board, draw, drawn

def loser():
    winners = 0
    drawn = [False]*(max(draws)+1)
    for draw in draws:
        drawn[draw] = True
        for board in boards:
            if len(boards) == 1:
                return boards[0], draw, drawn
            if won(board, drawn):
                boards.remove(board)

def calc_score(board, draw, drawn):
    sum = 0
    for row in board:
        for num in row:
            if drawn[num] is False:
                sum += num
    return sum*draw

#     print(f"{len(file_lines)} lines found, {file_bits} bits per line")

# Read the input file
draws, boards = read_input("input.txt")

win_board, win_draw, win_drawn = winner()
print(f"Winning board = {win_board} won at draw {win_draw}")
print(calc_score(win_board, win_draw, win_drawn))

lose_board, lose_draw, lose_drawn = loser()
print(f"Losing board = {lose_board} won at draw {lose_draw}")
print(calc_score(lose_board, lose_draw, lose_drawn))

