#!/bin/python

import socket
import os
import sys
import json

# Aplicação do usuário
class AgenteUsuario:
    
    def __init__( self, ipServidor, porta ):
        self.pid = os.getpid()
        self.endereco = ( ipServidor, porta )
        self.s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    # obtendo pid do agente usuário
    def get_mostrarPid( self ):
        return self.pid

    # transfere dados ao servidor e recebe resposta d'servidor
    def requisitarSoma( self, a, b ):

        dados = '{"a":' + str(a) + ',"b":' + str(b) + ',"pidcli":' + str(self.pid) + '}'
        charset = 'utf-8'

        try:

            self.s.send( bytes( dados, charset ) )
            resp = self.s.recv( 32 )
            print( json.loads( bytes.decode( resp, charset ) ) )

        finally:
            self.s.close()

    def conectar( self ):
        #verificando conexão
        try:

            self.s.connect( self.endereco )

            if len(sys.argv) == 5 :
                self.requisitarSoma( int(sys.argv[3]) , int(sys.argv[4]) )
            else:
                self.requisitarSoma( int(input('a>')), int(input('b>')) )

        except TimeoutError:
            print( 'ERRO: servidor especificado não disponível' )


# cliente.py [IP PORTA] [A B]

if ( len(sys.argv) == 5 ):
    #linha de comando
    app = AgenteUsuario( sys.argv[1] , int(sys.argv[2]) )
    app.conectar()
else:
    #interação direta
    app = AgenteUsuario( input( 'IP>' ), int(input( 'PORTA>' )) )
    app.conectar()
