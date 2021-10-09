import PySimpleGUI as sg


def janela_inicial():
    # layout janela
    sg.theme('DarkPurple1')
    layout = [
        [sg.Text('Dicionário de Tags do HTML',
                 font=('Helvetica', 25), justification='c'),
         sg.Image(filename='html.png')],
        [sg.Text('Adicionar tag ao dicionário', size=(30, 1)),
         sg.Checkbox('', default=False, key='add')],
        [sg.Text('Procurar tag específica', size=(30, 1)),
         sg.Checkbox('', default=False, key='buscar tag')],
        [sg.Text('Procurar por função específica', size=(30, 1)),
         sg.Checkbox('', default=False, key='buscar funcao')],
        [sg.Text('Ler todo o dicionário', size=(30, 1)),
         sg.Checkbox('', default=False, key='ler dict')],
        [sg.Button('', image_size=(24, 24),
                   image_filename='ok.png', key='ok'),
         sg.Button('', image_filename='clear.png', key='x')]
    ]
    # janela
    return sg.Window('Dicionário HTML', layout,
                     element_justification='center')


janela = janela_inicial()

while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == 'x':
        break