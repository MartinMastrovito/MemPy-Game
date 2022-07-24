import PySimpleGUI as sg
from itertools import cycle
from src.windows import board
from src.handlers import board as board_handler


def start():
    """
    Lanza la ejecución de la ventana del tablero
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana del tablero que capta sus eventos
    """
    player_1 = {"name": "Maria", "value": "X"}
    player_2 = {"name": "Marta", "value": "O"}
    turn = cycle([player_1, player_2])

    board_data = [[" "] * 3 for _i in range(3)]

    window = board.build(player_1, player_2, board_data)

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break

        if event.startswith("cell"):
            player = next(turn)
            board_data, winner = board_handler.play(player, window, event, board_data)

            if winner:
                sg.popup(f"¡Felicitaciones! Ha ganado {player['name']}")
                break

    return window
