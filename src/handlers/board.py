WIN_PLAYS = [
    [(0, 0), (1, 1), (2, 2)],  # diagonal
    [(0, 2), (1, 1), (2, 0)],  # diagonal
    [(0, 0), (0, 1), (0, 2)],  # vertical
    [(1, 0), (1, 1), (1, 2)],  # vertical
    [(2, 0), (2, 1), (2, 2)],  # vertical
    [(0, 0), (1, 0), (2, 0)],  # horizontal
    [(0, 1), (1, 1), (2, 1)],  # horizontal
    [(0, 2), (1, 2), (2, 2)],  # horizontal
]


def play(player, window, event, board_data):
    """
    Ejecuta una jugada sobre el tablero para un jugador:
    - Actualiza el tablero visual
    - Agrega el valor en board_data
    - Chequea si hay un ganador
    """
    window[event].update(player["value"])

    _prefix, x, y = event.split("-")
    board_data[int(x)][int(y)] = player["value"]

    winner = check_win(board_data, player["value"])

    return board_data, winner


def check_win(board, value):
    """
    Chequea si se cumple alguna de las jugadas ganadoras
    """
    for win_play in WIN_PLAYS:
        if check_play(win_play, board, value):
            return True


def check_play(win_play, board, value):
    """
    Chequea la si una jugada ganadora esta completa
    """
    # res = []
    # for x, y in win_play:
    #     res.append(board[x][y] == value)

    # return all(res)

    return all(board[x][y] == value for x, y in win_play)