def matrix_decorator(matrix):
    splitter = "---------"
    print(splitter)
    for item in matrix:
        print("|", " ".join(item), "|")
    print(splitter)


def check_winner(matrix, player):
    if check_win(matrix, player):
        return True
    if matrix[0][0] == player and matrix[1][1] == player and matrix[2][2] == player:
        return True
    if matrix[0][2] == player and matrix[1][1] == player and matrix[2][0] == player:
        return True
    matrix = list(map(list, zip(*matrix)))
    if check_win(matrix, player):
        return True
    return False


def check_win(matrix, player):
    for row in matrix:
        if row.count(player) == 3:
            return True


def check_impossible(matrix):
    x_count = sum(row.count("X") for row in matrix)
    o_count = sum(row.count("O") for row in matrix)
    if abs(x_count - o_count) > 1:
        return True
    return False


def check_draw(matrix):
    _count = sum(row.count("_") for row in matrix)
    if not check_winner(matrix, "X") and not check_winner(matrix, "O") and _count == 0:
        return True
    return False


def check_status(current_state):
    check_winner_x = check_winner(current_state, "X")
    check_winner_o = check_winner(current_state, "O")
    if check_impossible(current_state):
        s = "Impossible"
    elif check_winner_x and check_winner_o:
        s = "Impossible"
    elif check_winner_x:
        s = "X wins"
    elif check_winner_o:
        s = "O wins"
    elif check_draw(current_state):
        s = "Draw"
    else:
        s = "Game not finished"
    return s


def get_correct_coordinates(current_state):
    while True:
        coordinates_split = input("Enter the coordinates:").split()
        if len(coordinates_split) != 2:
            print("You should enter numbers!")
            continue
        x, y = coordinates_split
        if not (x.isdigit() and y.isdigit()):
            print("You should enter numbers!")
            continue
        x, y = int(x), int(y)
        if not (0 < x < 4) or not (0 < y < 4):
            print("Coordinates should be from 1 to 3!")
            continue
        x, y = 3 - y, x - 1
        if current_state[x][y] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            break
    return x, y


def main():
    inp = input("Enter cells:").strip().replace("_", " ")
    current_state = [list(inp[i:i + 3]) for i in range(0, 9, 3)]
    matrix_decorator(current_state)
    x, y = get_correct_coordinates(current_state)

    # print(x, y, *current_state)
    # new_value = input()
    current_state[x][y] = "X"
    # print(current_state[x][y])
    matrix_decorator(current_state)


main()

# status = check_status(current_state)
# print(status)
