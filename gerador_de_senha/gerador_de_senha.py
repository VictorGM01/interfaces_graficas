import PySimpleGUI as sg
import random
import string


class GeradorDeSenha:

    def __init__(self):
        # layout
        sg.theme('DarkBlack')
        layout = [
            [sg.Text('Gerador de Senhas', size=(20, 1),
                     font=('Helvetica', 20), justification='c')],
            [sg.Text('Senha Fraca', size=(19, 1)),
             sg.Checkbox('', default=False, key='senha fraca')],
            [sg.Text('Senha Intermediária', size=(19, 1)),
             sg.Checkbox('', default=False, key='senha intermediaria')],
            [sg.Text('Senha Forte', size=(19, 1)),
             sg.Checkbox('', default=False, key='senha forte')],
            [sg.Spin([x for x in range(1, 30)], initial_value=1, key='chars'),
             sg.Text('Quantidade de Caracteres')],
            [sg.Output(size=(40, 3))],
            [sg.Button('Gerar Senha')]
        ]
        # janela
        self.janela = sg.Window('Gerador de Senhas', layout,
                                element_justification='c')

    def iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            elif evento == 'Gerar Senha':
                if valores['senha fraca']:
                    senha_fraca = ''.join(random.choice(string.ascii_lowercase)
                                          for x in range(
                        int(valores['chars']))
                                          )
                    print(senha_fraca)
                if valores['senha intermediaria']:
                    senha_inter = ''.join(random.choice(string.ascii_letters +
                                                        string.digits)
                                          for x in range(
                        int(valores['chars']))
                                          )
                    print(senha_inter)


teste = GeradorDeSenha()
teste.iniciar()
