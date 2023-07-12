def print_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")

def check_win(board, player):
    if board[0] == board[1] == board[2] == player:
        return True
    elif board[3] == board[4] == board[5] == player:
        return True
    elif board[6] == board[7] == board[8] == player:
        return True
    elif board[0] == board[3] == board[6] == player:
        return True
    elif board[1] == board[4] == board[7] == player:
        return True
    elif board[2] == board[5] == board[8] == player:
        return True
    elif board[0] == board[4] == board[8] == player:
        return True
    elif board[2] == board[4] == board[6] == player:
        return True
    else:
        return False

def tic_tac_toe():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print_board(board)

    player1 = "X"
    player2 = "O"
    current_player = player1

    while True:
        move = int(input("Enter a position (1-9) for " + current_player + ": "))
        if board[move-1] == " ":
            board[move-1] = current_player
            print_board(board)
            if check_win(board, current_player):
                print(current_player + " wins!")
                break
            elif " " not in board:
                print("It's a tie!")
                break
            else:
                if current_player == player1:
                    current_player = player2
                else:
                    current_player = player1
        else:
            print("That position is already taken!")
