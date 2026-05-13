import os
import time
import sys

# Classe de operações de sistema usando comandos dependendo do SO
class OSOperations:
    #Executa o comando de limpar a tela, dependendo de qual sistema operacional
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    #Fecha o programa, limpando a tela e mandando uma saudação
    @staticmethod
    def close_program():
        OSOperations.clear()

        print('Até mais')

        time.sleep(3)

        OSOperations.clear()

        sys.exit(0)