#!/bin/python

import socket
import os
import sys
import json
import time
import random

# Aplicação do usuário
class AgenteUsuario:

    CARGATAMANHO = 64
    CHARSET = 'utf-8'

    def __init__( self, ipServidor, porta ):
        self.pid = os.getpid()
        self.cpid = self.gerarClientPid()
        print(f'{{"pid":{self.pid},"cpid":{self.cpid}}}')
        self.endereco = ( ipServidor, porta )
        self.s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    # obtendo pid do processo do agente usuário
    def get_mostrarPid( self ):
        return self.pid

    # gera o pid de cliente com base no UNIX
    # TIMESTAMP corrente no momento da instânciação
    # da classe. cpid
    def gerarClientPid( self ):
        return random.randint( 0, int( time.time() ) )

    # transfere dados ao servidor e recebe resposta d'servidor
    # emitindo-a na stdout do cliente
    def requisitarSoma( self, a, b ):

        dados = '{"a":' + str(a) + ',"b":' + str(b) + ',"pid":' + str(self.pid) + ',"cpid":' + str(self.cpid) + '}'

        try:

            self.s.send( bytes( dados, self.CHARSET ) )
            resp = self.s.recv( self.CARGATAMANHO )
            print( json.loads( bytes.decode( resp, self.CHARSET ) ) )

        finally:
            self.s.close()

    def conectar( self ):
        #VERIFICANDO CONEXÃO
        try:

            self.s.connect( self.endereco )

            if len(sys.argv) == 5 :
                self.requisitarSoma( int(sys.argv[3]) , int(sys.argv[4]) )
            else:
                self.requisitarSoma( int(input('a>')), int(input('b>')) )

        except socket.error as e: 
            print ("ERRO DE CONEXÃO: %s" % e)

        finally:
            self.s.close()



if ( len(sys.argv) == 5 ):
    # cliente.py [IP PORTA]
    app = AgenteUsuario( sys.argv[1] , int(sys.argv[2]) )
    print(f'{{"servidor":{sys.argv[1]},"porta":{sys.argv[2]}}}')
    app.conectar()
else:
    ip = input( 'IP> ' )
    porta = int( input( 'PORTA> ' ) )
    app = AgenteUsuario( ip, porta )
    print(f'{{"servidor":{ip},"porta":{porta}}}')
    app.conectar()
