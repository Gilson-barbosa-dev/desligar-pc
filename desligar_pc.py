from logging import shutdown
import os
from pickle import FALSE, TRUE
import PySimpleGUI as sg

#Layout do desligamento
layout = [ 
        [sg.Text('Tempo de desligamento'), sg.Input(key='tempo', size=(15,6))],
        [sg.Text('Escolha a ação            '),sg.Combo(['shutdown /s /t','shutdown -a',],key='acao', size=(13,6))],
        [sg.Button('Avançar')]
]

#Janela de exibição
Janela = sg.Window('Desligar PC', layout)


#Leitura dos dados

while TRUE:
    eventos, valores = Janela.read()
    if eventos == sg.WINDOW_CLOSED:
            break
    
    tempo = valores['tempo']
    acao = valores['acao']

print(acao)

Janela.close()

os.system(f'{acao} {tempo}')
