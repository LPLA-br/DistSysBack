import socket       # comunicação
import _thread    # paralelismo
import os           # funcionalidades do sistema (UNIX/LINUX)
import json

# SERVIDOR TCP C/python

"""
socket()  Instância um "endpoint"
bind()    Acopla uma porta ao socket instânciado
listen()  Escuta aguardando por conexões
 accept()  Aceitação de conexão
  connect() Estabelecimento da comunicação
   send()    Mandar dados
   recv()    Receber dados
  shutdown()   Encerrar conexão?
close()   Exterminar socket
"""

# servidor que faz divisões
# cria socket, atende requisição, mata socket
class Servidor:

    def __init__( self, porta ):

        self.HOST = socket.gethostbyname( socket.gethostname() )
        self.PORTA = porta

        self.id = os.getpid()

        self.s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.s.bind( ( self.HOST, self.PORTA ) )
        self.s.listen( 4 )

    # processa divisão para {"a":10,"b":2} requisitado PROTECTED
    def divisao( self, byteStr ):

        dic = {}
        encode = 'utf-8'

        dic = json.loads( byteStr.decode( encode ) )
        resultado = ( dic['a'] / dic['b'] )
        resp = '{\"r\":' + str( resultado ) + '}'
        return bytes( resp, encode )
            
    def aceitarConexao( self, cli_sock, addr ):
            while True:
                dados = cli_sock.recv( 32 )
                print(dados)
                if dados:
                    cli_sock.send( self.divisao( dados ) )
                    break
            cli_sock.close()

    def escutar( self ):
        while True:
            conn, addr = self.s.accept()
            _thread.start_new_thread( self.aceitarConexao, ( conn, addr ) )
        self.s.close()

app = Servidor( 8080 )
app.escutar()

