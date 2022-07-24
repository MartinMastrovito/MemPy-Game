import PySimpleGUI as sg
from src.windows import menu
from src.component import board


def start():
    """
    Lanza la ejecución de la ventana del menú
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    window = menu.build()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break

        if event == "-play-":
            window.hide()
            board.start()
            window.un_hide()

        if event == "-settings-":
            pass

        if event == "-score-":
            pass

    return window
