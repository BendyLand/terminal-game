'''
# Project Objectives:
#! Build a terminal program using Python
#! Add at least one interactive feature using input()
#! Use Git version control
#! Use the command line and file navigation
# Write a technical blog post on the project
'''


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

player_one = input("Please enter a name for player 1: ") or "Player 1"
player_two = input("Please enter a name for player 2: ") or "Player 2"
player_turn = player_one
player_token = 'x' if player_turn == player_one else 'o'

def play_round():
    game_won = False
    while not game_won:
        global player_turn
        player_token = 'x' if player_turn == player_one else 'o'
        print(f"It's {player_turn}'s ({player_token}) turn!")
        print("Here is the current board: ")
        display_board()

        player_choice = -1
        while not (0 <= player_choice <= 7):
            player_choice = int(input("Please select a column to play your token (1 - 7): ")) - 1
            if not (0 <= player_choice <= 6):
                print("Invalid input, please try again!\n")

        for row in p:
            if row[player_choice] == '_':
                row[player_choice] = player_token
                game_won = check_win(player_turn, player_choice, player_token)
                break
            if row6[player_choice] != '_':
                print('Column is full, pick another one!\n')
                play_round()

        display_board()
        player_turn = player_one if player_turn == player_two else player_two

if __name__ == "__main__":
    print("\nWelcome to Connect Four!")
    play_round()
    