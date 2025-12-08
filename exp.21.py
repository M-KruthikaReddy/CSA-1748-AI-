

board = [' ' for _ in range(9)]

def print_board():
    row1 = '|'.join(board[0:3])
    row2 = '|'.join(board[3:6])
    row3 = '|'.join(board[6:9])
    print(row1)
    print('-' * 5)
    print(row2)
    print('-' * 5)
    print(row3)

def player_move(icon):
    if icon == 'X':
        player = 1
    else:
        player = 2

    print(f"Player {player}'s turn")

    while True:
        try:
            choice = int(input("Enter your move (1-9): ").strip())
            if 1 <= choice <= 9 and board[choice - 1] == ' ':
                board[choice - 1] = icon
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def is_victory(icon):
    return (
        (board[0] == icon and board[1] == icon and board[2] == icon) or
        (board[3] == icon and board[4] == icon and board[5] == icon) or
        (board[6] == icon and board[7] == icon and board[8] == icon) or
        (board[0] == icon and board[3] == icon and board[6] == icon) or
        (board[1] == icon and board[4] == icon and board[7] == icon) or
        (board[2] == icon and board[5] == icon and board[8] == icon) or
        (board[0] == icon and board[4] == icon and board[8] == icon) or
        (board[2] == icon and board[4] == icon and board[6] == icon)
    )

def is_draw():
    return ' ' not in board

while True:
    print_board()

    player_move('X')
    if is_victory('X'):
        print_board()
        print("X Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a Draw!")
        break

    print_board()

    player_move('O')
    if is_victory('O'):
        print_board()
        print("O Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a Draw!")
        break
