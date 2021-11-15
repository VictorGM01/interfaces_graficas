import PySimpleGUI as sg
import random
import string
import pyperclip


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
            [sg.Spin([x for x in range(1, 60)], initial_value=1, key='chars'),
             sg.Text('Quantidade de Caracteres')],
            [sg.Output(size=(40, 3))],
            [sg.Button('', button_color=('#F0F0F0', '#F0F0F0'),
                       image_filename='baseline_vpn_key_black_24dp.png',
                       key='Gerar Senha'),
             sg.Button('', button_color=('#F0F0F0', '#F0F0F0'),
                       image_filename='copy.png', key='copy'),
             sg.Button('', button_color=('#F0F0F0', '#F0F0F0'),
                       image_filename='save.png', key='save'),
             sg.Button('', button_color=('#F0F0F0', '#F0F0F0'),
                       image_filename='baseline_clear_black_24dp.png', key='x'
                       )]
        ]
        # janela
        self.janela = sg.Window('Gerador de Senhas', layout,
                                element_justification='c')

    def iniciar(self):
        # verifica os eventos que estão acontecendo (Ex.: clique nos botões)
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED or evento == 'x':
                break  # interrompe o código caso o usuário feche a janela

            # acontece caso o botão de gerar senha seja pressionado
            elif evento == 'Gerar Senha':

                # executa quando o checkbox "senha fraca" é marcado
                if valores['senha fraca']:

                    # gera senha com caracteres minúsculos
                    global senha_fraca
                    senha_fraca = ''
                    for c in range(valores['chars']):
                        senha_fraca += random.choice(string.ascii_lowercase)

                    print(senha_fraca)

                # executa quando o checkbox "senha intermediária" é marcado
                if valores['senha intermediaria']:

                    # gera senha com caracteres minúsculos e maiúsculos
                    global senha_inter
                    senha_inter = ''
                    for c in range(valores['chars']):
                        senha_inter += random.choice(string.ascii_letters +
                                                     string.digits)

                    print(senha_inter)

                # executa quando o checkbox "senha forte" é marcado
                if valores['senha forte']:

                    # gera senha com caracteres minúsculos e maiúsculos,
                    # dígitos e caracteres especiais
                    global senha_forte
                    senha_forte = ''
                    for c in range(valores['chars']):
                        senha_forte += random.choice(string.ascii_letters +
                                                     string.digits +
                                                     "@#!&$#%*/ç.;:?¨()" +
                                                     "[]{}|,^~+-¨'_=°ªº")

                    print(senha_forte)

            elif evento == 'copy':
                if valores['senha fraca']:
                    pyperclip.copy(senha_fraca)

                elif valores['senha intermediaria']:
                    pyperclip.copy(senha_inter)

                elif valores['senha forte']:
                    pyperclip.copy(senha_forte)


teste = GeradorDeSenha()
teste.iniciar()
