from logging import shutdown
import os
from pickle import FALSE, TRUE
from tkinter.tix import Tree
import PySimpleGUI as sg

desligar = 'shutdown /s /t'
cancelar = 'shutdown -a'

#Layout do desligamento
layout = [ 
        [sg.Text('Tempo de desligamento'), sg.Input(key='tempo', size=(15,6))],
        [sg.Radio('Desligar',desligar, key='acao'), sg.Radio('Cancelar',cancelar)],
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

        if acao == True:
                acao = desligar
        elif acao == False:
                acao = cancelar        
        
Janela.close()

os.system(f'{acao} {tempo}')
