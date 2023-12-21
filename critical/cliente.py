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

    CARGATAMANHO = 256
    CHARSET = 'utf-8'

    def __init__( self, ipServidor, porta, prioridade ):
        self.pid = os.getpid()
        self.cpid = self.gerarClientPid()
        self.prioridade = prioridade
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

    #Envia dados e recebe respostas.
    def enviarRequisicao(self,dados):# void
        try:
            self.s.send( bytes( dados, self.CHARSET ) )
            resp = self.s.recv( self.CARGATAMANHO )
            print( bytes.decode( resp, self.CHARSET ) )
        finally:
            self.s.close()

    def operacaoBancaria(self,valor,tipo):# void
        dados=''
        if tipo == 'saque':
            dados='{"tipo":"'+str(tipo)+'","valor":'+str(valor)+',"pid":'+str(self.pid)+',"cpid":'+str(self.cpid)+',"pri":'+str(self.prioridade)+'}'
            print(f'\npid: {self.pid} | saque de {valor}R$ com prioridade: {self.prioridade}\n')
        elif tipo == 'deposito':
            dados='{"tipo":"'+str(tipo)+'","valor":'+str(valor)+',"pid":'+str(self.pid)+',"cpid":'+str(self.cpid)+',"pri":'+str(self.prioridade)+'}'
            print(f'\npid: {self.pid} | depósito de {valor}R$ com prioridade: {self.prioridade}\n')
        else:
            print('operação bancária inválida')
            return
        self.enviarRequisicao(dados)

    def conectar( self ):
        try:
            self.s.connect( self.endereco )
            if len(sys.argv) == ARGS_NUM :
                self.operacaoBancaria( int(sys.argv[4]) , str(sys.argv[5]) )
        except socket.error as e: 
            print ("ERRO DE CONEXÃO: %s" % e)
        finally:
            self.s.close()


if sys.argv[1] == '--help' :
    print('comando SERVIDOR PORTA PRIORIDADE VALOR TIPO_DE_OPERAÇÃO_BANCÁRIA')
    exit()

if ( len(sys.argv) == ARGS_NUM ):
    # ip porta prioridade valor tipo_de_operação
    app = AgenteUsuario( sys.argv[1] , int(sys.argv[2]), sys.argv[3] )
    app.conectar()
else:
    print('use --help para ver a lista de argumentos de linha de comando')
