import socket
import os

# Aplicação do usuário
# nível de abstração: baixo
class AgenteUsuario:
    
    def __init__( self ):
        self.pid = os.getpid()

    # faz requisição de recurso para o servidor
    def requisitar( self, ipAlvo ):
        print('não implementado')
        pass

    # retorna PID do processo cliente
    def get_mostrarPid( self ):
        print( self.pid )
        return self.pid

app = AgenteUsuario()
app.pid()
