import PySimpleGUI as sg
sg.main_get_debug_data()

def criar_tarefas():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas',Layout=linha,key='container')]
        [sg.Button('Nova tarefa'),sg.Button('Resetar')]
        
    ]

    return sg.Window('Tudo List',Layout=layout,finalize=True)
janela = criar_tarefas()
while True:
    event, value, = janela.read()