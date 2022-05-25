#imports
import random
import numpy as np

def random_move():
    # bot makes random moves
    x = random.randint(1,3)
    y = random.randint(1,3)
    move = f"{x},{y}"

    if validate_move(move):
        return move
    else:
        return random_move()

def complex_move():
    # if selected move will stop opponent victory or guarantee own victory, perform the move, else return random move
    for i in range(1,4):
        for j in range(1,4):
            dummy_board = np.copy(board)
            move = f"{i},{j}"
            if validate_move(move):
                perform_move(move=move, player=True, chosen_board=dummy_board)
                if victory_check(symbol="X", chosen_board=dummy_board):
                    return move

                else:
                    dummy_board = np.copy(board)
                    perform_move(move=move, player=False, chosen_board=dummy_board)
                    if victory_check(symbol="O", chosen_board=dummy_board):
                        return move

    return random_move()





# create the board
board = np.empty((3,3), dtype="str")
board[:] = "-"

# call the board
def print_board():
    for i in range(0,3):
        print(board[i][0],board[i][1],board[i][2])


# check if move is valid
def validate_move(move):
    try:
        x = move.split(",")[0]
        y = move.split(",")[1]
    except IndexError:
        return False

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return False

    if x in [1,2,3] and y in [1,2,3]:
        if board[x-1,y-1] == "-":
            return True
    else:
        return False

# perform move by changing board
def perform_move(move, chosen_board, player=False ):
    X = int(move.split(",")[0])
    Y = int(move.split(",")[1])

    if player:
        chosen_board[X-1][Y-1] = "X"

    else:
        chosen_board[X-1][Y-1] = "O"

# recursive prompt
def prompt_player():
    player_move = input("Please enter your move: ")
    if validate_move(player_move):
        perform_move(move=player_move, player=True, chosen_board=board)
    else:
        print("Invalid choice, please try again.")
        prompt_player()


def victory_check(symbol, chosen_board=board):
    counter_d = 0
    counter_h = 0
    counter_v = 0

    for i in range(3):

        # check diagonal
        if chosen_board[i][i] == symbol:
            counter_d += 1

        # reset counters
        counter_h = 0
        counter_v = 0
        for j in range(3):
            # check for horizontal win
            if chosen_board[i][j] == symbol:
                counter_h += 1
            # check for vertical win
            if chosen_board[j][i] == symbol:
                counter_v += 1

            if counter_d == 3 or counter_h == 3 or counter_v == 3:
                return True

            elif chosen_board[0][2] == symbol and chosen_board[1][1] == symbol and chosen_board[2][0] == symbol:
                return True

    return False

def draw_check():
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != "-":
                count += 1

    if count == 9:
        return True

    else:
        return False


game = True

print("Please enter your moves as the row and column of the position you wish to occupy, separated by a comma,"
      " such as: '1,1' or '3,2'.")
while game:
    print_board()
    # player move
    prompt_player()
    print_board()
    if victory_check("X"):
        print("Congratulations! You win!")
        game = False
        break

    # check if the game is a draw
    if draw_check():
        print("The game is a draw!")
        game = False
        break

    # bot move
    bot_choice = complex_move()  ### change complex to random and all works
    perform_move(move=bot_choice, player=False,chosen_board=board)
    print(f"The computer chose: {bot_choice}")
    if victory_check("O"):
        print_board()
        print("You Lose!")
        game = False
        break




