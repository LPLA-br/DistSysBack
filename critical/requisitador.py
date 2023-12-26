#!/bin/python

import random
import sys
import os
import _thread
from time import sleep

if sys.argv[1] == '--help' or sys.argv[1] == '-h':
    print('./requisitador.py <IP> <REQ_NUM>')
    exit()

print(len(sys.argv))

servidor = sys.argv[1]
porta    = sys.argv[2]
requisicoes = int(sys.argv[3])

valor = 0
operacao = 'saque'
prioridade = 1

def operacaoAleatoria():
    n = random.randrange(0,2)
    if n == 1:
        return 'deposito'
    else:
        return 'saque'

def requisitarCliente():
    os.system(f'./cliente.py {servidor} {porta} {prioridade} {valor} {operacao}')

if requisicoes == 0:
    while True:
        sleep(2)

        valor = random.randrange( 0, 999 )
        prioridade = random.randrange( 1,4 )
        operacao = operacaoAleatoria()

        _thread.start_new_thread( requisitarCliente, () )
else:
    while requisicoes > 0:
        sleep(2)

        valor = random.randrange( 0, 999 )
        prioridade = random.randrange( 1,4 )
        operacao = operacaoAleatoria()

        _thread.start_new_thread( requisitarCliente, () )
        requisicoes -= 1

exit()

