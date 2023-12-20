#!/bin/python

import socket       # comunicação
import _thread      # paralelismo
import os           # funcionalidades do sistema (UNIX/LINUX)
import json
from time import sleep

# Aplicação com zona crítica para
# threads

# classe responsável pela
# fila de dados e requisições.
class Fila:

    def __init__(self):
        self.fila=[]

    def enfileirar(self, estrutura):
        self.fila.append(estrutura)

    def desenfileirar(self):
        if len(self.fila) > 0:
            return self.fila.pop(0)
        else:
            return 0

    # ordena prioridades conforme o campo "pri" número
    def ordenacaoInsercaoPrioridades( self ):

        if len(self.fila) <= 1:
            return

        # posicionais
        i=1
        j=0

        # armazena estrutura para troca de posições.
        prioridade={}

        while i < len(self.fila):
            prioridade = self.fila[i]
            j = i-1
            while ( not(j<0) and (prioridade['pri'] > self.fila[j]['pri']) ):
                self.fila[j+1] = self.fila[j]
                j -= 1
            self.fila[j+1] = prioridade
            i += 1

    #retorna as prioridade de uma
    #fila do primeiro elemento até o
    #ultimo.
    def get_pri_fila(self):
        retorno = []
        for elemento in self.fila:
            retorno.append( { "pri" : elemento['pri'] } )
        return retorno

    def get_tam(self):
        return len(self.fila)

# servidor que faz divisões
# cria socket, atende requisição, mata socket
class Servidor:

    CARGATAMANHO = 256
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
        self.fila = Fila()
        self.saldo = 1000

    def saque( self, byteStr ):# bytestring
        d = {}
        d = json.loads( byteStr.decode( self.CHARSET ) )
        resp = f'\nsem resposta'
        if d['valor'] > self.saldo:
            resp = f'\n\tpid:{d["pid"]} | prioridade:{str(d["pri"])} | Saque maior que o saldo atual de: {self.saldo}'
        else:
            self.saldo -= d['valor']
            resp = f'\n\tpid:{d["pid"]} | prioridade:{str(d["pri"])} | Valor sacado: {d["valor"]} saldo corrente: {self.saldo}'
        return bytes( resp, self.CHARSET )

    def deposito( self, byteStr ):# bytestring
        d = {}
        d = json.loads( byteStr.decode( self.CHARSET ) )
        self.saldo += d['valor']
        resp = f'\n\tpid:{d["pid"]} | prioridade:{str(d["pri"])} | Valor depositado: {d["valor"]} saldo corrente: {self.saldo}'
        return bytes( resp, self.CHARSET )

    def validador( self, byteStr ):# bytestring
        d = {}
        d = json.loads( byteStr.decode( self.CHARSET ) )
        if 'valor' in d and 'tipo' in d and 'pid' in d: 
            if   d['tipo'] == 'saque':
                return self.saque( byteStr )
            elif d['tipo'] == 'deposito':
                return self.deposito( byteStr )
        else:
            return b'{"err":400,"msg":"bad request"}'

    # thread
    def aceitarConexao( self, cli_sock, addr ):
        while True:
            dados = cli_sock.recv( self.CARGATAMANHO )
            if dados:
                novoDic = json.loads( dados.decode( self.CHARSET ) )
                print( f'{{ "clienteip":{addr[0]},"clienteporta":{addr[1]},"cpid":{novoDic["cpid"]},"pid":{novoDic["pid"]},"a":{novoDic["a"]},"b"{novoDic["b"]},"pri":{novoDic["pri"]} }}' )
                novoDic.update( {"concli": cli_sock} )
                self.fila.enfileirar( novoDic )
                self.fila.ordenacaoInsercaoPrioridades()
                break


    # desenfileira, atende requisição e fecha conexão.
    # retorna True para atendimento e False para fila vazia
    def atenderConexao(self):
        estrutura = self.fila.desenfileirar()
        if estrutura == 0:
            return False
        else:
            cli_sock = estrutura.pop("concli")
            cli_sock.send( self.validador( bytes( json.dumps(estrutura) , self.CHARSET) ) )
            cli_sock.close()
            return True

    #atende às requisições na fila para temporizadorAssincrono()
    def atenderFila(self):
        while True:
            sleep(1)
            if self.atenderConexao():
                print(f'{{"filaTamanho":{self.fila.get_tam()}}}')
            else:
                break

    # N segundos para a execução do método de atender a fila.
    # método semi-bloqueante.
    def temporizadorAssincrono(self, tempo):
        self.temporizador = True
        sleep(tempo)
        self.atenderFila()
        self.temporizador = False


    # MÉTODO CENTRAL.
    def escutar( self ):
        while True:
            if self.temporizador == False:
                _thread.start_new_thread( self.temporizadorAssincrono, (20,) )
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

