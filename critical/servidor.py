#!/bin/python

import socket       # comunicação
import _thread      # paralelismo
import os           # funcionalidades do sistema (UNIX/LINUX)
import json
from time import sleep

# Threadas não seguem nos métodos de
# saque e deposito enquanto self.bloquear
# tiver sido definido como verdadeiro por
# outra thread.

class Servidor:

    CARGATAMANHO = 1024
    CHARSET = 'utf-8'
    temporizador = False

    def __init__( self, porta ):
        self.HOST = socket.gethostbyname( socket.gethostname() )
        self.PORTA = porta
        self.id = os.getpid()
        print(f'{{"serverip":{self.HOST},"porta":{self.PORTA},"serverpid":{self.id}}}\n')
        self.s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.s.bind( ( self.HOST, self.PORTA ) )
        self.s.listen( 4 )
        self.saldo = 1000
        self.bloquear = False

    def saque( self, byteStr ):# bytestring
        d = json.loads( byteStr.decode( self.CHARSET ) )
        resp = f'\nsem resposta'
        while self.bloquear == True:
            sleep(1)
            print(f'bloqueando o pid: {d["pid"]}')
        self.bloquear = True
        sleep(1)
        if d['valor'] > self.saldo:
            resp = f'\n\tpid:{d["pid"]} | prioridade:{str(d["pri"])} | Saque maior que o saldo atual de: {self.saldo}'
        else:
            self.saldo -= d['valor']
            resp = f'\n\tpid:{d["pid"]} | prioridade:{str(d["pri"])} | Valor sacado: {d["valor"]} saldo corrente: {self.saldo}'
        sleep(1)
        self.bloquear = False
        return bytes( resp, self.CHARSET )

    def deposito( self, byteStr ):# bytestring
        d = json.loads( byteStr.decode( self.CHARSET ) )
        while self.bloquear == True:
            print(f'bloqueando o pid: {d["pid"]}')
            continue
        self.bloquear = True
        sleep(2)
        self.saldo += d['valor']
        resp = f'\n\tpid:{d["pid"]} | prioridade:{str(d["pri"])} | Valor depositado: {d["valor"]} saldo corrente: {self.saldo}'
        self.bloquear = False
        return bytes( resp, self.CHARSET )

    def validador( self, byteStr ):# bytestring
        d = json.loads( byteStr.decode( self.CHARSET ) )
        if 'valor' in d and 'tipo' in d and 'pid' in d: 
            if   d['tipo'] == 'saque':
                return self.saque( byteStr )
            elif d['tipo'] == 'deposito':
                return self.deposito( byteStr )
        else:
            return b'{"err":400,"msg":"bad request"}'

    def aceitarConexao( self, conn, addr ):
        while True:
            dados = conn.recv( self.CARGATAMANHO )
            if dados:
                d = json.loads( dados.decode( self.CHARSET ) )
                print( f'{{ "clienteip":{addr[0]},"clienteporta":{addr[1]},"cpid":{d["cpid"]},"pid":{d["pid"]},"pri":{d["pri"]},"valor":{d["valor"]},"tipo":{d["tipo"]} }}' )
            res = self.validador( dados )
            conn.send( res )
        conn.close()

    # MÉTODO CENTRAL.
    def escutar( self ):
        while True:
            conn, addr = self.s.accept()
            _thread.start_new_thread( self.aceitarConexao, ( conn, addr ) )
        app.encerrarSocket()
                    

    # encerra o socket do servidor
    def encerrarSocket():
        self.s.close()

app = Servidor( 8080 )
try:
    app.escutar()
except KeyboardInterrupt:
    print( 'servidor interrompido' )

