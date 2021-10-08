import PySimpleGUI as sg
import random
import string


class GeradorDeSenha:

    def __init__(self):
        # layout
        sg.theme('DarkPurple6')
        layout = [
            [sg.Text('Gerador de Senhas', size=(17, 1))],
            [sg.Text('Senha Fraca', size=(19, 1)),
             sg.Checkbox('', default=True, key='senha fraca')],
            [sg.Text('Senha Intermediária', size=(19, 1)),
             sg.Checkbox('', default=True, key='senha intermediaria')],
            [sg.Text('Senha Forte', size=(19, 1)),
             sg.Checkbox('', default=True, key='senha forte')],
            [sg.Spin([x for x in range(1, 30)], initial_value=1),
             sg.Text('Quantidade de Caracteres')]
        ]
        # janela
        self.janela = sg.Window('Gerador de Senhas', layout)

    def iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            elif evento == 'senha fraca':
                senha = ''.join(random.choice(string.ascii_lowercase)
                                for x in range(
                                int(valores['Quantidade de Caracteres']))
                                )
                print(senha)


