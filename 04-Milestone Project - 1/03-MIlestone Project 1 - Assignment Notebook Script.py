# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Milestone Project 1
# ## Congratulations on making it to your first milestone!
# You've already learned a ton and are ready to work on a real project.
# 
# Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.
# 
# Here are the requirements:
# 
# * 2 players should be able to play the game (both sitting at the same computer)
# * The board should be printed out every time a player makes a move
# * You should be able to accept input of the player position and then place a symbol on the board
# 
# Feel free to use Google to help you figure anything out (but don't just Google "Tic Tac Toe in Python" otherwise you won't learn anything!) Keep in mind that this project can take anywhere between several hours to several days.
# 
# There are 4 Jupyter Notebooks related to this assignment:
# 
# * This Assignment Notebook
# * A "Walkthrough Steps Workbook" Notebook
# * A "Complete Walkthrough Solution" Notebook
# * An "Advanced Solution" Notebook
# 
# I encourage you to just try to start the project on your own without referencing any of the notebooks. If you get stuck, check out the next lecture which is a text lecture with helpful hints and steps. If you're still stuck after that, then check out the Walkthrough Steps Workbook, which breaks up the project in steps for you to solve. Still stuck? Then check out the Complete Walkthrough Solution video for more help on approaching the project!

# %%
def display_welcome():
    print('Welcome to my tic tac toe game!')
    print("You'll see two boards. One is the numbers you can pick. The other, the current state of the game")
    print("Player 1 goes first, and has the 'X', pick between 1 and 9")
    print("Player 2 then goes, and has the 'O'")


# %%
display_welcome()


# %%
def show_rule_board():
    print("\nDecision Board\n")
    print("1   2   3")
    print("4   5   6")
    print("7   8   9")


# %%
show_rule_board()


# %%
def get_win_conditions():
    return [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3],
            [4, 5, 6], [7, 8, 9], [1, 5, 9], [7, 5, 3]]


# %%
def get_draw_condition():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


# %%
def get_space(choices, spot):
    if spot in choices['X']:
        return 'X'
    elif spot in choices['O']:
        return 'O'
    
    return ' '


# %%
def draw_active_board(choices):
    print("\nActive Board\n")
    # Could be a loop?
    print(" " + get_space(choices, 1) + " | " + get_space(choices, 2) + " | " + get_space(choices, 3))
    print("-----------")
    print(" " + get_space(choices, 4) + " | " + get_space(choices, 5) + " | " + get_space(choices, 6))
    print("-----------")
    print(" " + get_space(choices, 7) + " | " + get_space(choices, 8) + " | " + get_space(choices, 9))


# %%
choices = {'X': [], 'O': []}
draw_active_board(choices)


# %%
choices = {'X' : [1, 2, 3], 'O' : [4, 5, 6]}

draw_active_board(choices)


# %%
def gameon():
    choice = "wrong"

    while choice not in ['Y', 'N']:
        choice = input("Would you like to keep playing? Y or N")

        if choice not in ['Y', 'N']:
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")

    return choice == 'Y'


# %%
gameon()


# %%
def choice_open(choices, choice):
    if not choice in choices['X'] and not choice in choices['O']:
        return True

    return False


# %%
choices = {'X' : [1, 2, 3], 'O' : [4, 5, 6]}


# %%
choice_open(choices, 1)


# %%
choice_open(choices, 7)


# %%
def update_choices(choices, choice, symbol):
    choices[symbol].append(choice)
    draw_active_board(choices)


# %%
player_choices = {'X' : [], 'O' : []}
draw_active_board(player_choices)

update_choices(player_choices, 1, 'X')
update_choices(player_choices, 2, 'O')


# %%
def user_choice(choices, symbol):
    choice = "wrong"
    
    if symbol == 'X':
        print("\nPlayer 1 turn ('X')")
    else:
        print("\nPlayer 2 turn ('O')")

    while not choice.isdigit():
        choice = input("Choose a number: ")
        
        if not choice.isdigit():
            print("Sorry, but you did not enter an integer. Please try again.")
            continue

        choice_int = int(choice)

        if choice_int < 1 or choice_int > 9:
            print("Sorry, you must pick an integer between 1 and 9")
            choice = "wrong"

        if not choice_open(choices, int(choice)):
            print("That spot has already been picked.")
            choice = "wrong"

    update_choices(choices, choice_int, symbol)


# %%
player_choices = {'X' : [], 'O' : []}
user_choice(player_choices, 'X')


# %%
def game_over(choices):
    win_conds = get_win_conditions()
    draw_conds = get_draw_condition()

    for win_cond in win_conds:
        if set(choices['X']) == set(win_cond):
            print("\nPlayer 1 wins!")
            return True
        elif set(choices['O']) == set(win_cond):
            print("\nPlayer 2 wins!")
            return True
        elif set(choices['X'] + choices['O']) == set(draw_conds):
            print("\nThe game is a draw!")
            return True

    return False 


# %%
player_choices = {'X' : [], 'O' : []}
print(game_over(player_choices))

player_choices = {'X' : [1, 2, 3], 'O' : []}
print(game_over(player_choices))

player_choices = {'X' : [4, 5, 6], 'O' : []}
print(game_over(player_choices))

player_choices = {'X' : [1, 3, 4, 6, 8], 'O' : [2, 5, 7, 9]}
print(game_over(player_choices))


# %%
# Putting it all together
from IPython.display import clear_output

game_on = True
player_one = 'X'
player_two = 'O'

while game_on:
    clear_output()

    player_choices = {'X' : [], 'O' : []}
    display_welcome()

    gameover = False
    
    while not gameover:
        show_rule_board()
        user_choice(player_choices, player_one)
        gameover = game_over(player_choices)

        if gameover:
            break

        user_choice(player_choices, player_two)
        gameover = game_over(player_choices)

    game_on = gameon()


# %%



