#!/bin/python

import socket
import os
import sys
import json
import time
import random

ARGS_NUM = 6

# Aplicação do usuário
class AgenteUsuario:

    CARGATAMANHO = 64
    CHARSET = 'utf-8'

    def __init__( self, ipServidor, porta, prioridade ):
        self.pid = os.getpid()
        self.cpid = self.gerarClientPid()
        self.prioridade = prioridade
        print(f'{{"servidor":"{ipServidor}","porta":{porta},"my_pid":{self.pid},"my_cpid":{self.cpid},"pri":{self.prioridade}}}')
        self.endereco = ( ipServidor, porta )
        self.s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    # obtendo pid do processo do agente usuário
    def get_mostrarPid( self ):
        return self.pid

    # gera o pid de cliente com base no UNIX
    # TIMESTAMP corrente no momento da instânciação
    # da classe. cpid
    def gerarClientPid( self ):
        return random.randint( 0, 999 )

    def get_pid(self):
        return this.pid

    def get_cpid(self):
        return this.cpid

    # transfere dados ao servidor e recebe resposta d'servidor
    # emitindo-a na stdout do cliente
    def requisitarSoma( self, a, b ):
        dados = '{"a":' + str(a) + ',"b":' + str(b) + ',"pid":' + str(self.pid) + ',"cpid":' + str(self.cpid) + ',"pri":' + str(self.prioridade) + '}'
        try:
            self.s.send( bytes( dados, self.CHARSET ) )
            resp = self.s.recv( self.CARGATAMANHO )
            print( '\t', json.loads( bytes.decode( resp, self.CHARSET ) ) )
        finally:
            self.s.close()

    def conectar( self ):
        try:
            self.s.connect( self.endereco )
            if len(sys.argv) == ARGS_NUM :
                self.requisitarSoma( int(sys.argv[3]) , int(sys.argv[4]) )
        except socket.error as e: 
            print ("ERRO DE CONEXÃO: %s" % e)
        finally:
            self.s.close()


if sys.argv[1] == '--help' :
    print('comando SERVIDOR PORTA N1 N2 PRIORIDADE={1,2,3}')
    exit()

if ( len(sys.argv) == ARGS_NUM ):
    # cliente.py [IP PORTA]
    app = AgenteUsuario( sys.argv[1] , int(sys.argv[2]), sys.argv[5] )
    app.conectar()
else:
    print('use --help para ver a lista de argumentos de linha de comando')
