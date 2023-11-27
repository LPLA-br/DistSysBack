#!/bin/python

import random
import sys
import os
import _thread
from time import sleep

if len(sys.argv) < 4:
    print('./requisitador.py <IP> <PORTA> <NÚMERO_DE_CHAMADAS>')

servidor = sys.argv[1]
porta    = sys.argv[2]
requisicoes = int(sys.argv[3])

numero1 = 0
numero2 = 0
prioridade = 1


def requisitarCliente():
    os.system(f'./cliente.py {servidor} {porta} {numero1} {numero2} {prioridade}')

try:
    while True:
        sleep(1)
        numero1 = random.randrange( 0, 9999 )
        numero2 = random.randrange( 0, 9999 )
        prioridade = random.randrange( 1,4 )

        if ( requisicoes > 0 ):
            _thread.start_new_thread( requisitarCliente, () )
        elif ( requisicoes == 0 ):
            try:
                requisicoes = int(input('>'))
            except ValueError:
                print('Insira um inteiro meu chapa !!! definindo para 10')
                requisicoes = 10

        requisicoes -= 1

except KeyboardInterrupt:
    print( 'Requisitador encerrado' )

