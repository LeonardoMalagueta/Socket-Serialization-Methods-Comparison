#FINALIZADO, #ESTA OK ✅

import socket
from auth import auth
from echo import echo
from soma import soma
from timestamp import timestamp
from status import status
from historico import historico
from logout import logout
import os
import sys

##########################
#--VARIAVEIS DO SERVIDOR--
SERVER_IP = "3.88.99.255"
SERVER_PORT = 8082
##########################


#-- Clear do terminal --
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#-- Encerrar programa --
def sair(sock):
    print("[ 🛑 ] Programa finalizado, encerrando socket")
    sock.close()
    print(f"\n Prima a telca ENTER para fechar o terminal...")
    input("> ").strip()
    sys.exit()

############################## MAIN ###################################
def main():
    clear()

#===================== Conexao com o servidor =========================
    try:
        sock = socket.socket()
        sock.settimeout(10)
        sock.connect((SERVER_IP, SERVER_PORT))
        print("[✅ ] Conectado com sucesso!")
    except Exception as e:
        print(f"[❌] Servidor de PROTOBUF nao responde: {e}")
        sair(sock)
#======================================================================

#=================== Dicionario de funções e loop =====================
    token = None
    erro_counter = 0
    operacoes = {# dicionariod e operações pra cada funcao em arquivo
        "1": lambda: echo(sock, token),
        "2": lambda: soma(sock, token),
        "3": lambda: timestamp(sock, token),
        "4": lambda: status(detalhado,sock, token),
        "5": lambda: historico(sock,token)
    }
#======================================================================

    #loop principal
    while True:

        
        #======================= Autenticação ==========================
        while not token:
            try:
                print(f"[➡️ ] Digite sua matricula para autenticação:")
                matricula = input("Matricula: ").strip()
                if matricula == "x":    #queira sair sem errar 3x
                    sair(sock)
                [token, nome] = auth(sock, matricula)
                clear()
                print("\n[✅ ] Bem vindo:", nome , " seu token de acesso é: ",token)
                erro_counter = 0
            except Exception as e:
                erro_counter = erro_counter+1
                if erro_counter >= 3:   #sair ao errar 3x
                    sair(sock)
                else:
                    print(f"tente novamente")
        #===============================================================

         
        
        #==================== loop de operações ========================
        while True:
            print("\nEscolha uma operação para realizar no servidor:")
            print("[1] Echo")
            print("[2] Soma")
            print("[3] Timestamp")
            print("[4] Status do servidor")
            print("[5] Historico")
            print("[6] Logout")
            print("[0] Sair")
            op = input("> ").strip()    #recebe a operação
            
            #tratativa para a Status (0,4 e 5)
            #----------------------------------------------------------
            if op == "4":  
                clear()
                print("Digite o tipo de informação desejada:")
                print("[0] Simples")
                print("[1] Detalhado")
                detalhado = input("> ").strip()
            #----------------------------------------------------------
            if op == "0":
                clear()
                logout(sock,token)
                sair(sock)
                break
            #----------------------------------------------------------
            if op == "6":
                clear()
                logout(sock,token)
                token = None
                break
            #----------------------------------------------------------

            acao = operacoes.get(op)
            clear()
            if acao:
                acao()
            else:
                print("Operação inválida!")
        #======================================================================
########################### FIM DA MAIN ###############################



#Rodar a main
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Programa encerrado")