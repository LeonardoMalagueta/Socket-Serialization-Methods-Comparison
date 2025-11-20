#ESTA OK ✅
import socket, json
from datetime import datetime

def timestamp_json(sock,token):
    print("\n[TIMESTAMP] Requisitando informações de tempo ao servidor...:")

    msg = {
        "tipo":     "operacao",
        "operacao": "timestamp",
        "token":    token
    #tipos: "autenticar", "operacao", "info", "logout"
    #operacao: "echo" "soma" "timestamp" "status" "historico"
    #parametros: "mensagem" "numeros"
    }

    #Transforma converte e envia a mensagem
    msg = json.dumps(msg)+"\n"         #converte o dicionario python pra json
    
    try:
        sock.sendall(msg.encode())         #encode - transforma em bytes pro socket enviar
        resposta = sock.recv(4096).decode()#recebimento da msg do servidor
    except Exception as e:
        print(f"[TIMESTAMP] Erro no servidor:", {e})
        return
    
    ########### DEBUG ##############
    #Print da mensagem montada
    #print(msg)           
    #Print da mensagem recebida
    #print("Resposta:", resposta )
    #################################

    #=================== Tratamento da resposta ==================
    resposta = json.loads(resposta)
    if resposta.get("sucesso","") is True:
        print(f"[TIMESTAMP][✅] Consulta realizada com sucesso")
        print(f"Dados de tempo do servidor:",resposta.get("resultado").get("timestamp_formatado"))
        print(f"Microsegundos:             ",resposta.get("resultado").get("microsegundo"))
        print(f"Timestamp em Unix:         ",resposta.get("resultado").get("timestamp_unix"))
        print(f"timestamp em ISO:          ",resposta.get("resultado").get("timestamp_iso"))
    else:
        print(f"[TIMESTAMP][❌] Consulta falhou: ", resposta.get("mensagem",""))
    #=============================================================