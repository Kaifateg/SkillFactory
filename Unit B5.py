board = {}
board_full = board.fromkeys(["0:0", "0:1", "0:2", "1:0", "1:1", "1:2", "2:0", "2:1", "2:2"], "-")

players = {}

win_if = {
    ("0:0", "0:1", "0:2"),
    ("1:0", "1:1", "1:2"),
    ("2:0", "2:1", "2:2"),
    ("0:0", "1:1", "2:2"),
    ("0:2", "1:1", "2:0"),
    ("0:0", "1:0", "2:0"),
    ("0:1", "1:1", "2:1"),
    ("0:2", "1:2", "2:2")
}

def print_board():
    print(" ", 0, 1, 2,
    f'\n0 {board_full["0:0"]} {board_full["0:1"]} {board_full["0:2"]}'
    f'\n1 {board_full["1:0"]} {board_full["1:1"]} {board_full["1:2"]}'
    f'\n2 {board_full["2:0"]} {board_full["2:1"]} {board_full["2:2"]}')

def win_check(name):
    board_mask = set(players[name])
    winner = bool([True for rule in win_if if len(board_mask.intersection(rule)) == 3])
    return winner

def start():
    print(f'\nWelcome to the Tic-tac-toe game.\n'
          f'\nRules: Input number to make a move on board. For example: 0:1. '
          f'\nThe first number indicates vertical position.'
          f'\nThe second number indicates horizontal position.'
          f'\nInput 0 to complete the game.\n')
    player_1 = str(input("Enter first player name:"))
    player_2 = str(input("\nEnter second player name:"))
    players.update({player_1: [], player_2: []})
    now_plays = player_1
    step = 1
    while True:
        print_board()
        number = str(input("Input number:"))
        if number == "0":
            print("Game over.")
            break
        elif number in set(board_full):
            if board_full[number] == "-" and now_plays == player_1:
                players[now_plays].append(number)
                board_full[number] = "X"
            elif board_full[number] == "-" and now_plays == player_2:
                players[now_plays].append(number)
                board_full[number] = "O"
            else:
                print("This number is busy. Сhoose a different number.")
                continue
            if win_check(now_plays):
                print(f'\n{now_plays} winner!')
                print_board()
                break
            else:
                if step == 9:
                    print("Nobody wins. Game over.")
                    break
                else:
                    step += 1
            now_plays = player_2 if now_plays == player_1 else player_1
        else:
            print("Wrong number. See the rules and try again.")
            continue

start()