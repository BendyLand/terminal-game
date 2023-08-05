'''
Project Objectives:
Build a terminal program using Python
Add at least one interactive feature using input()
Use Git version control
Use the command line and file navigation
Write a technical blog post on the project
'''

row6 = ['_', '_', '_', '_', '_', '_', '_']
row5 = ['_', '_', '_', '_', '_', '_', '_']
row4 = ['_', '_', '_', '_', '_', '_', '_']
row3 = ['_', '_', '_', '_', '_', '_', '_']
row2 = ['_', '_', '_', '_', '_', '_', '_']
row1 = ['_', '_', '_', '_', '_', '_', '_']

p = [row1, row2, row3, row4, row5, row6]

def display_board():
    r6 = f"|{'|'.join(row6)}|"
    r5 = f"|{'|'.join(row5)}|"
    r4 = f"|{'|'.join(row4)}|"
    r3 = f"|{'|'.join(row3)}|"
    r2 = f"|{'|'.join(row2)}|"
    r1 = f"|{'|'.join(row1)}|"

    print(f"\n\t{r6}\n\t{r5}\n\t{r4}\n\t{r3}\n\t{r2}\n\t{r1}\n\t 1 2 3 4 5 6 7\n")

print("Welcome to Connect Four!")
player_one = input("Please enter a name for player 1 (this player will go first): ") or "Player 1"
player_two = input("Please enter a name for player 2: ") or "Player 2"
player_turn = player_one

print(f"It's {player_turn}'s turn!")
print("Here is the current board: ")
display_board()
player_choice = int(input("Please select a column to play your token: ")) - 1
row1[player_choice] = 'x'
display_board()


"""
Example of inputting a token:

col = int(input("Column: ")) - 1
p[5][col] = 'x'
display_board()
"""
