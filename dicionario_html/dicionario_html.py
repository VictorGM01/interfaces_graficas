import PySimpleGUI as sg


def janela_inicial():
    # layout janela
    sg.theme('DarkPurple1')
    layout = [
        [sg.Text('Dicionário de Tags do HTML',
                 font=('Helvetica', 25), justification='c')],
        [sg.Text('Adicionar tag ao dicionário', size=(30, 1)),
         sg.Checkbox('', default=False, key='add')],
        [sg.Text('Procurar tag específica', size=(30, 1)),
         sg.Checkbox('', default=False, key='buscar tag')],
        [sg.Text('Procurar por função específica', size=(30, 1)),
         sg.Checkbox('', default=False, key='buscar funcao')],
        [sg.Text('Ler todo o dicionário', size=(30, 1)),
         sg.Checkbox('', default=False, key='ler dict')],
        [sg.Button('', button_color=('#F0F0F0', '#F0F0F0'),
                   image_filename='circulo.png')]

    ]