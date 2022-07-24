import PySimpleGUI as sg


def conf():
    """
    Construye la ventana del menú de configuracion del juego
    """
    layout = [
        [sg.Text('Elegir Texto de Partida', key="-textP-")],
        [sg.Text('Texto de victoria'),sg.InputText()],[sg.Text('Texto de derrota'),sg.InputText()],[sg.Text('Conteo final'),sg.InputText()],
        [sg.Text('Cant de Casilleros: '),sg.Button('8x8', size=(5, 2), key="ocho"),sg.Button('16x16', size=(5, 2), key="dieciseis"),sg.Button('20x20', size=(5, 2), key="veinte")],
        [sg.Text('Cantidad de coincidencias: '),sg.Button('Dos',key='dos',size=(5, 2)),sg.Button('Cuatro',key='cuatro',size=(5, 2)),sg.Button('Seis',key='seis',size=(5, 2))],
        [sg.Text('Tipo de Elemento de la Casilla')],[sg.Button('Palabras', size=(10, 2),key="pala"),sg.Button('Imagenes y Palabras', size=(10, 2),key="palaimg")],
        [sg.Text('Ayuda In-Game')],[sg.Button('Con Ayuda', size=(10, 2), key="ayudasi"),sg.Button('Sin Ayuda', size=(10, 2), key="ayudano")],
        [sg.Text('Tiempo total de partida')],#completar
        [sg.ColorChooserButton('Paleta de colores a usar')]
    ]

    board = sg.Window('Login').Layout(layout)
    board.read()
    return board

conf()