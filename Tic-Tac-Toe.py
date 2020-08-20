import numpy
import random

""" The Tic Tac Toe game"""
""" THis game is between a player and computer that randomly chooses its position.
the user is by default assigned as 1 and the computer is 2.
user can choose his position on own whereas computer randomly chooses. This
 game can only be played once """

# board_to_display()
'''
This function displays the tic tac toe board to the player
for choosing his desired location
'''


def board_to_display():
    table = [['00', '10', '20'], ['01', '11', '21'], ['02', '12', '22']]
    for row in zip(*table):
        print(" ".join(row))


# checks if the board has any horizontal match
'''this function checks if there is any straight horizontal lines.
for this any row must have three elements compulsory'''


def horizontal_row_match(board):
    frow = []
    srow = []
    trow = []
    for j in range(0, 3):
        frow.append(board[0][j])
    for j in range(0, 3):
        srow.append(board[1][j])
    for j in range(0, 3):
        trow.append(board[2][j])
    if (all(ele == frow[0] == 1 and ele != 0 for ele in frow)) or \
            (all(ele == srow[0] == 1 and ele != 0 for ele in srow)) or \
            (all(ele == trow[0] == 1 and ele != 0 for ele in trow)):
        return {"status": True, "Player": 1}
    elif (all(ele == frow[0] == 2 and ele != 0 for ele in frow)) or \
            (all(ele == srow[0] == 2 and ele != 0 for ele in srow)) or \
            (all(ele == trow[0] == 2 and ele != 0 for ele in trow)):
        return {"status": True, "Player": 2}
    else:
        return {"status": False}


# checks if the board has any vertical match
'''this function checks if there is any straight vertical lines.
for this any column must have three elements compulsory'''


def vertical_column_match(board):
    fcol = []
    scol = []
    tcol = []
    for j in range(0, 3):
        fcol.append(board[j][0])
    for j in range(0, 3):
        scol.append(board[j][1])
    for j in range(0, 3):
        tcol.append(board[j][2])
    if (all(ele == fcol[0] == 1 and ele != 0 for ele in fcol)) or \
            (all(ele == scol[0] == 1 and ele != 0 for ele in scol)) or \
            (all(ele == tcol[0] == 1 and ele != 0 for ele in tcol)):
        return {"status": True, "Player": 1}
    elif (all(ele == fcol[0] == 2 and ele != 0 for ele in fcol)) or \
            (all(ele == scol[0] == 2 and ele != 0 for ele in scol)) or \
            (all(ele == tcol[0] == 2 and ele != 0 for ele in tcol)):
        return {"status": True, "Player": 2}
    else:
        return {"status": False}


# checks if there is a diagonal match
'''this function checks if there is any straight diagonal lines.
for this any diagonal must have three elements compulsory'''


def diagonal_match(board):
    fdiag = []
    sdiag = []
    for row in range(0, 3):
        for col in range(0, 3):
            if row == col:
                fdiag.append(board[row][col])
                if row == 1 and col == 1:
                    sdiag.append(board[row][col])
            elif row == 0 and col == 2:
                sdiag.append(board[row][col])
            elif row == 2 and col == 0:
                sdiag.append(board[row][col])
    if (all(ele == fdiag[0] == 1 and ele != 0 for ele in fdiag)) or \
            (all(ele == sdiag[0] == 1 and ele != 0 for ele in sdiag)):
        return {"status": True, "Player": 1}
    elif (all(ele == fdiag[0] == 2 and ele != 0 for ele in fdiag)) or \
        (all(ele == sdiag[0] == 2 and ele != 0 for ele in sdiag)):
        return {"status": True, "Player": 2}
    else:
        return {"status": False}


''' This is the main function that takes user's and computer's input for 
filling it in the tic tac toe board. if the position has been filled, concerned player has to 
 choose positions again. for all rounds greater than equal to 5, the check for winning starts.
 if there is a win the game stops. if after 9 rounds there is no win, it is a tie'''


def main():
    board = numpy.zeros([3, 3])
    row_lock = []
    user_symbol = 1
    print("HI, USER YOUR SYMBOL WILL BE 1 IN THE GAME AND COMPUTER WILL BE 2")
    count = 0
    while count < 9:
        if count % 2 == 0:
            print("--------------USER'S TURN---------------")
            print(f"Hi, player {user_symbol}, please choose your desired position")
            board_to_display()
            user_row = int(input("choose row:"))
            user_column = int(input("choose column:"))
            user_value = 1
            while (count != 0) and ((user_row, user_column) in row_lock):
                print(f"ENTER AGAIN, {(user_row, user_column)} POSITION IS FILLED")
                user_row = int(input("choose row:"))
                user_column = int(input("choose column:"))
                user_value = 1
        else:
            print("------------COMPUTER'S TURN---------------")
            computer_row = random.randint(0, 2)
            computer_column = random.randint(0, 2)
            computer_value = 2
            while (count != 0) and ((computer_row, computer_column) in row_lock):
                computer_row = random.randint(0, 2)
                computer_column = random.randint(0, 2)
                computer_value = 2
            user_row = computer_row
            user_value = computer_value
            user_column = computer_column
            print(f" Computer has chosen: {(user_row, user_value)}")

        board[user_row][user_column] = user_value
        row_lock.append((user_row, user_column))
        count = count + 1
        print("GAME TILL NOW ===> \n", board)
        if count >= 5:
            row_check = horizontal_row_match(board)
            column_check = vertical_column_match(board)
            diagonal_check = diagonal_match(board)
            if row_check['status']:
                print(f"GAME WON IN {count} MOVES, PLAYER: {row_check['Player']} IS WINNER")
                break
            elif column_check['status']:
                print(f"GAME WON IN {count} MOVES, PLAYER: {column_check['Player']} IS WINNER")
                break
            elif diagonal_check['status']:
                print(f"GAME WON IN {count} MOVES, PLAYER: {diagonal_check['Player']} IS WINNER")
                break
            else:
                print(f"GAME PLAYED {count} TIMES, IT IS A TIE")

    print("FINAL RESULT ======>\n", board)


main()
