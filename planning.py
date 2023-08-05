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

p = [row6, row5, row4, row3, row2, row1]

def display_board():
    r6 = f"|{'|'.join(row6)}|"
    r5 = f"|{'|'.join(row5)}|"
    r4 = f"|{'|'.join(row4)}|"
    r3 = f"|{'|'.join(row3)}|"
    r2 = f"|{'|'.join(row2)}|"
    r1 = f"|{'|'.join(row1)}|"

    print(\
        f"""
        {r6}
        {r5}
        {r4}
        {r3}
        {r2}
        {r1}
        """
    )

print("Welcome to Connect Four!")
player_one = input("Please enter a name for player 1 (this player will go first): ") or "Player 1"
player_two = input("Please enter a name for player 2: ") or "Player 2"

print(f"It's {player_one}'s turn")
print("Here is the current board:")
print(\
    f"""
     1 2 3 4 5 6 7
    Please select a column to play a piece.
    """
)
col = int(input("Column: ")) - 1
p[5][col] = 'x'
display_board()
