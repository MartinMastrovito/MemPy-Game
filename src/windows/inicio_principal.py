import PySimpleGUI as sg


def prin():
    """
    Construye la ventana del ingreso del juego
    """
    layout = [
        [sg.Button('Login',key="-login-", size=(50, 2))],
        [sg.Button('Sala de Juego', size=(50, 2), key="-juego-")],
        [sg.Button('Puntajes', size=(50, 2), key="-puntajes-")],
        [sg.Button('Estadisticas', size=(50, 2), key="-estadisticas-")],
        [sg.Button('Configuracion', size=(50, 2), key="-config-")],
        [sg.Button('Salir', size=(50, 2), key="-salir-")],
    ]

    board = sg.Window('Login').Layout(layout)
    return board