row6 = ['_', '_', '_', '_', '_', '_', '_']
row5 = ['_', '_', '_', '_', '_', '_', '_']
row4 = ['_', '_', '_', '_', '_', '_', '_']
row3 = ['_', '_', '_', '_', '_', '_', '_']
row2 = ['_', '_', '_', '_', '_', '_', '_']
row1 = ['_', '_', '_', '_', '_', '_', '_']

p = [row1, row2, row3, row4, row5, row6]

def check_win(turn, choice, p_token):
    def check_diagonal_win(tokens):
        if tokens >= 4:
            print(f"Game over!\n{turn} wins!")
            return True
        return False

    # check rows
    for row in p:
        tokens = 0
        for item in row:
            if item == p_token:
                tokens += 1
                if tokens >= 4:
                    print(f"Game over!\n{turn} wins!")
                    return True
            else:
                tokens = 0

    # check columns
    col_tokens = 0
    for row in p:
        if row[choice] == p_token:
            col_tokens += 1
            if col_tokens >= 4:
                print(f"Game over!\n{turn} wins!")
                return True
        else:
            col_tokens = 0

    # check diagonal (bottom left to top right)
    r_index, c_index = 0, 0
    for row in range(len(p) - 1, -1, -1):
        for col in range(len(p[row])):
            if p[row][col] == p_token:
                tokens = 1
                r_index, c_index = row, col
                while r_index - 1 >= 0 and c_index + 1 < len(p[0]):
                    r_index -= 1
                    c_index += 1
                    if p[r_index][c_index] == p_token:
                        tokens += 1
                        if check_diagonal_win(tokens):
                            return True
                    else:
                        break

    # check diagonal (bottom right to top left)
    for row in range(len(p) - 1, -1, -1):
        for col in range(len(p[row]) - 1, -1, -1):
            if p[row][col] == p_token:
                tokens = 1
                r_index, c_index = row, col
                while r_index - 1 >= 0 and c_index - 1 >= 0:
                    r_index -= 1
                    c_index -= 1
                    if p[r_index][c_index] == p_token:
                        tokens += 1
                        if check_diagonal_win(tokens):
                            return True
                    else:
                        break
    
    return False

def display_board():
    r6 = f"|{'|'.join(row6)}|"
    r5 = f"|{'|'.join(row5)}|"
    r4 = f"|{'|'.join(row4)}|"
    r3 = f"|{'|'.join(row3)}|"
    r2 = f"|{'|'.join(row2)}|"
    r1 = f"|{'|'.join(row1)}|"

    print(f"\n\t{r6}\n\t{r5}\n\t{r4}\n\t{r3}\n\t{r2}\n\t{r1}\n\t 1 2 3 4 5 6 7\n")
