import PySimpleGUI as sg


def janela_inicial() -> sg.Window:
    # layout
    sg.theme('DarkPurple1')
    layout = [
        [sg.Text('Dicionário de Tags do HTML',
                 font=('Helvetica', 25), justification='c'),
         sg.Image(filename='icons\html.png')],
        [sg.Text('Adicionar tag ao dicionário', size=(30, 1)),
         sg.Checkbox('', default=False, key='add')],
        [sg.Text('Procurar tag específica', size=(30, 1)),
         sg.Checkbox('', default=False, key='buscar tag')],
        [sg.Text('Procurar por função específica', size=(30, 1)),
         sg.Checkbox('', default=False, key='buscar funcao')],
        [sg.Text('Ler todo o dicionário', size=(30, 1)),
         sg.Checkbox('', default=False, key='ler dict')],
        [sg.Button('', image_size=(24, 24),
                   image_filename='icons\ok.png', key='ok'),
         sg.Button('', image_filename='icons\clear.png', key='x')]
    ]
    # janela
    return sg.Window('Dicionário HTML', layout,
                     element_justification='center')


def janela_adiciona_tag() -> sg.Window:
    sg.theme('DarkPurple1')
    # layout
    layout = [
        [sg.Text('Adicionar uma Nova Tag ao Dicionário',
                 font=('Helvetica', 15), justification='c'),
         sg.Image(filename='icons\icon_add_html.png')],
        [sg.Text('Nome da Tag', size=(15, 1)),
         sg.Input(key='nome da tag', size=(30, 1))],
        [sg.Text('Função da Tag', size=(15, 1)),
         sg.Input(key='função da tag', size=(30, 1))],
        [sg.Output(size=(50, 1))],
        [sg.Button('', image_filename=r'icons\add.png', key='adicionar tag'),
         sg.Button('', image_filename='icons\clear.png',
                   key='cancelar adição')]
    ]
    # janela
    return sg.Window('Adicionar Tag', layout,
                     element_justification='c')


def janela_busca_tag() -> sg.Window:
    sg.theme('DarkPurple1')
    # layout
    layout = [
        [sg.Text('Pesquisar uma Tag Específica', font=('Helvetica', 15),
                 justification='c'),
         sg.Image(filename='icons\icon_search.png')],
        [sg.Text('Nome da Tag', size=(15, 1)),
         sg.Input(key='nome da tag - busca', size=(30, 1))],
        [sg.Text('Resultado:', size=(10, 1))],
        [sg.Output(size=(50, 2))],
        [sg.Button('', image_filename='icons\icon_btn_busca.png',
                   key='buscar tag'),
         sg.Button('', image_filename='icons\clear.png',
                   key='cancelar busca')]
    ]
    # janela
    return sg.Window('Buscar Tag', layout, element_justification='c')


def janela_busca_funcao():
    sg.theme('DarkPurple1')
    # layout
    layout = [
        [sg.Text('Pesquisar Função Específica', font=('Helvetica', 15),
                 justification='c'),
         sg.Image(filename='icons\icon_busca_func.png')],
        [sg.Text('Função', size=(10, 1)),
         sg.Input(key='função da tag', size=(30, 1))],
        [sg.Text('Resultado(s):', size=(10, 1))],
        [sg.Output(size=(50, 2))],
        [sg.Button('', image_filename='icons\icon_btn_busca.png',
                   key='buscar função'),
         sg.Button('', image_filename='icons\clear.png',
                   key='cancelar pesquisa')]
    ]
    # janela
    return sg.Window('Buscar Função', layout, element_justification='c')


def janela_ler_dicionario():
    sg.theme('DarkPurple1')
    # layout
    layout = [
        [sg.Text('Dicionário de Tags HTML', font=('Helvetica', 20),
                 justification='c'),
         sg.Image(filename='icons\icon_read_dict.png')],
        [sg.Output(size=(50, 15))],
        [sg.Button('', image_filename=r'icons\btn_read.png',
                   key='ler dicionário'),
         sg.Button('', image_filename='icons\clear.png',
                   key='cancelar leitura')]
    ]
    # janela
    return sg.Window('Ler Dicionário', layout, element_justification='c')


janela = janela_ler_dicionario()

while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == 'cancelar leitura':
        break