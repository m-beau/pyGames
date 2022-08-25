#!/usr/bin/env python
# coding: utf-8

# In[95]:


import numpy as np
import getpass


# # Paper, Rock, Scissors!

# In[232]:


player1 = None
player2 = None
winner = None

authorized = ['Paper', 'Rock', 'Scissors']

name1 = input("Player 1's name:")
name2 = input("Player 2's name:")

while winner is None:
    while player1 is None:
        play = getpass.getpass(prompt=f"{name1}: Paper, Rock, Scissors?")
        print("\r")
        if play not in authorized:
            print('Check your spelling!')
            continue
        player1 = play

    while player2 is None:
        play = input(f"{name2}: Paper, Rock, Scissors?")
        if play not in authorized:
            print('Check your spelling!')
            continue
        player2 = play
                      
    if player1 == player2:
        print("Tie!")
        player1 = None
        player2 = None

    if player1 == "Paper":
        if player2 == "Rock":
            winner = name1
        elif player2 == "Scissors":
            winner = name2

    if player1 == "Rock":
        if player2 == "Paper":
            winner = name2
        elif player2 == "Scissors":
            winner = name1
            
    if player1 == "Scissors":
        if player2 == "Rock":
            winner = name2
        elif player2 == "Paper":
            winner = name1

loser = [n for n in [name1,name2] if n!=winner][0]
print(f"{winner} crushed {loser}!")


# # Hangman

# In[233]:


word_to_guess = "blitzkrieg"


# In[234]:


hangman_states = ["",
"""
___
""",
"""
 |
 |
 |
 |
 |
___
""",
"""
  _____
 |
 |
 |
 |
 |
___
""",
"""
  _____
 |  !
 |
 |
 |
 |
___
""",
"""
  _____
 |  !
 |  O
 |
 |
 |
___
""",
"""
  _____
 |  !
 |  O
 |  1
 |  1
 | 
___
""",
"""
  _____
 |  !
 |  O
 | /1
 |  1
 |
___
""",
"""
  _____
 |  !
 |  O
 | /1\\
 |  1
 | 
___
""",
"""
  _____
 |  !
 |  O
 | /1\\
 |  1
 | / 
___
""",
"""
  _____
 |  !
 |  O
 | /1\\
 |  1
 | / \\
___
"""]


# In[235]:


current_guess = ["_"]*len(word_to_guess)
spaces =  [" "]*len(word_to_guess)
hangman_state = 0
tried_letters = []
while current_guess != word_to_guess:
    guess_disp = list(zip(current_guess, spaces))
    guess_disp = [item for sublist in guess_disp for item in sublist]
    guess_disp = "".join(guess_disp)[:-1]
    
    disp_str = "\nGuess the word:\n"+guess_disp+'\n'+hangman_states[hangman_state]+'\n'
    
    print(disp_str)
    
    # Process input
    letter = input("Pick a letter (a-z):")
    if len(letter)!=1:
        print("You should input one letter!")
    if ord(letter)<97 or ord(letter)>122:
        print("Your letter must be lowercase between a and z!")
        continue
    if letter in tried_letters:
        print(f"You already tried {letter}!")
        continue
    tried_letters.append(letter)
    
    # Game rules
    if letter not in word_to_guess:
        print("Whoops! Wrong letter")
        hangman_state+=1
        if hangman_state == len(hangman_states)-2:
            print("Bobby is hanging there...")
        elif hangman_state == len(hangman_states)-1:
            print(f"You left Bobby down... The word was {word_to_guess}. Try again!")
            print(hangman_states[hangman_state])
            break
    else:
        print("Good job, you found a letter!")
        letter_i = letter == np.array([w for w in word_to_guess])
        current_guess = np.array([w for w in current_guess])
        current_guess[letter_i] = letter
        current_guess = "".join(list(current_guess))
        
    if current_guess == word_to_guess:
        print("\nCongrats, you saved Bobby!!!")


# # Tic, tac, toe!

# In[236]:


import numpy as np

def check_winning_board(board):
    col_sums = np.sum(board, axis = 0)
    row_sums = np.sum(board, axis = 1)
    diag_sum1 = np.trace(board)
    diag_sum2 = np.trace(np.fliplr(board))
    
    all_values = np.append(col_sums, row_sums)
    all_values = np.append(all_values, [diag_sum1, diag_sum2])
    
    return 3 in all_values

def display_board(board):
    board_display = []
    for board_row in board:
        board_display_row = []
        for board_val in board_row:
            if board_val==2:
                board_val = 'x'
            elif board_val==1:
                board_val = 'o'
            else:
                board_val = ' '
            board_display_row.append(board_val)
        board_display.append(board_display_row)
    board_display_render = f"""
    {board_display[0][0]}|{board_display[0][1]}|{board_display[0][2]}
    _____
    {board_display[1][0]}|{board_display[1][1]}|{board_display[1][2]}
    _____
    {board_display[2][0]}|{board_display[2][1]}|{board_display[2][2]}
    """
    print(board_display_render)
    
def board_is_full(board):
    for row in board:
        for val in row:
            if val == 0:
                return False
    return True


# In[133]:


name1 = input("Player 1's name:")
name2 = input("Player 2's name:")


# In[237]:


# initialize empty board
board = \
[[0,0,0],
 [0,0,0],
 [0,0,0]]

winner = None


while winner is None:
    
    player1_played = None
    player2_played = None
    
    while player1_played is None and winner is None:
        # make player 1 pick location
        display_board(board)
        loc_1 = input("Player 1 pick a location (row, column)")
        if len(loc_1) !=3:
            print("You must input your location following this format: 'row column'")
            continue
        row = int(loc_1[0])
        col = int(loc_1[2])
        if row < 1 or row > 3:
            print("You must pick a row between 1 and 3!")
            continue
        if col < 1 or col > 3:
            print("You must pick a column between 1 and 3!")
            continue

        # check whether location already busy with player 1 or player 2 (0)
        value = board[row-1][col-1]
        if value == 0:
            # if check passed, add 1 to picked location
            board[row-1][col-1] = 1
        else:
            print("Location already busy - pick another one!")
            continue

        # make board with only values of 1 (replace 2s with 0s)
        board_1 = []
        for board_row in board:
            board_1_row = []
            for board_val in board_row:
                if board_val==2:
                    board_val = 0
                board_1_row.append(board_val)
            board_1.append(board_1_row)

        # compare board against winning combinations to check if player 1 won!
        if check_winning_board(board_1):
            winner = 1
            display_board(board)
            print("Player 1 won!")
        player1_played = True
        
    if board_is_full(board) and winner is not None:
        print("That's a tie!")
        winner = 0

    while player2_played is None and winner is None:
        # make player 2 pick location
        display_board(board)
        loc_2 = input("Player 2 pick a location (row, column)")
        if len(loc_2) !=3:
            print("You must input your location following this format: 'row column'")
            continue
        row = int(loc_2[0])
        col = int(loc_2[2])
        if row < 1 or row > 3:
            print("You must pick a row between 1 and 3!")
            continue
        if col < 1 or col > 3:
            print("You must pick a column between 1 and 3!")
            continue

        # check whether location already busy with player 1 or player 2 (0)
        value = board[row-1][col-1]
        if value == 0:
            # if check passed, add 1 to picked location
            board[row-1][col-1] = 2
        else:
            print("Location already busy - pick another one!")
            continue

        # make board with only values of 1 (replace 2s with 0s)
        board_2 = []
        for board_row in board:
            board_2_row = []
            for board_val in board_row:
                if board_val==1:
                    board_val = 0
                board_2_row.append(board_val)
            board_2.append(board_2_row)

        # compare board against winning combinations to check if player 1 won!
        if check_winning_board(board_2):
            winner = 2
            display_board(board)
            print("Player 2 won!")
        player2_played = True
        
    if board_is_full(board) and winner is not None:
        print("That's a tie!")
        winner = 0


# In[ ]:




