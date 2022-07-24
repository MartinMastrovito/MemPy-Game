import PySimpleGUI as sg


def sala():
    """
    Construye la ventana de la sala del juego
    """
    layout = [
        [sg.Text('sala de juego',size=(100,100))],
    ]

    board = sg.Window('Login').Layout(layout)
    return board