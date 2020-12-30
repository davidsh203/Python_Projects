# Tic Tac Toe Game
player1 = 'X'
player2 = 'O'
player1_win = 0
player2_win = 0
count_step = 0
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Welcome to Tic Tac Toe Game")


def printing_board(arr):
    print("-------------")
    print("|", arr[0], "|", arr[1], "|", arr[2], "|")
    print("-------------")
    print("|", arr[3], "|", arr[4], "|", arr[5], "|")
    print("-------------")
    print("|", arr[6], "|", arr[7], "|", arr[8], "|")
    print("-------------")


def gets_from_user1():
    global count_step
    printing_board(board)
    user1 = int(input("Choose number from board to put X: "))
    if user1 < 1 or user1 > 9:
        print("Invalid number, the number need to between 1-9")
        gets_from_user1()
    elif board[user1 - 1] == player1 or board[user1 - 1] == player2:
        print("The place is choosen")
        gets_from_user1()
    for x in board:
        if user1 == x:
            board[x - 1] = player1
            count_step += 1


def gets_from_user2():
    global count_step
    printing_board(board)
    user2 = int(input("Choose number from board to put O: "))
    if user2 < 1 or user2 > 9:
        print("Invalid number, the number need to between 1-9")
        gets_from_user2()
    elif board[user2 - 1] == player1 or board[user2 - 1] == player2:
        print("The place is choosen")
        gets_from_user2()
    for x in board:
        if user2 == x:
            board[x - 1] = player2
            count_step += 1


def winning(arr, who_win):
    if arr[0] == arr[1] and arr[0] == arr[2] and arr[0] == who_win:
        return True
    elif arr[3] == arr[4] and arr[3] == arr[5] and arr[3] == who_win:
        return True
    elif arr[6] == arr[7] and arr[6] == arr[8] and arr[6] == who_win:
        return True
    elif arr[0] == arr[3] and arr[0] == arr[6] and arr[0] == who_win:
        return True
    elif arr[1] == arr[4] and arr[1] == arr[7] and arr[1] == who_win:
        return True
    elif arr[2] == arr[5] and arr[2] == arr[8] and arr[2] == who_win:
        return True
    elif arr[0] == arr[4] and arr[0] == arr[8] and arr[0] == who_win:
        return True
    elif arr[2] == arr[4] and arr[2] == arr[6] and arr[2] == who_win:
        return True
    return False


def reset_board():
    global board
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def start_game():
    global count_step
    global player1_win
    global player2_win
    gets_from_user1()
    gets_from_user2()
    while not winning(board, player1):
        gets_from_user1()
        if winning(board, player1):
            printing_board(board)
            player1_win += 1
            break
        if count_step == 9:
            printing_board(board)
            break
        gets_from_user2()
        if winning(board, player2):
            printing_board(board)
            player2_win += 1
            break
    if count_step == 9 and not winning(board, player1) and not winning(board, player2):
        print("The game it ended in a draw")
        print("The result is: " + str(player1_win) + " wins to Player X and " + str(player2_win) + " wins to Player O")
    if winning(board, player1):
        print("Player X winner!")
        print("Player X with " + str(player1_win) + " wins, and Player O with " + str(player2_win) + " wins")
    if winning(board, player2):
        print("Player O winner!")
        print("Player O with " + str(player2_win) + " wins, and Player X with " + str(player1_win) + " wins")

    another_game = input("Do you want another game y/n? ")
    while another_game != 'Y' and another_game != 'y' and another_game != 'N' and another_game != 'n':
        print("Invalid letter, please enter again!")
        another_game = input("Do you want another game y/n? ")
    if another_game == 'Y' or another_game == 'y':
        count_step = 0
        reset_board()
        start_game()
    elif another_game == 'N' or another_game == 'n':
        print("Thanks for the game!")


start_game()
