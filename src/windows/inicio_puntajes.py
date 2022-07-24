import PySimpleGUI as sg


def punt():
    """
    Construye la ventana de puntajes del juego
    """
    layout = [
        [sg.Text('Igresar  Nick',key="-nick-"),sg.InputText()],
        [sg.Button('OK', size=(50, 2), key="-ok-")],
        [sg.Button('Ayuda', size=(50, 2), key="-help-")],
        [sg.Button('Volver', size=(50, 2), key="-volver-")],
    ]

    board = sg.Window('Login').Layout(layout)
    return board