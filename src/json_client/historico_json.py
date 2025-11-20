#ESTA OK ✅
import socket, json
from datetime import datetime

def historico_json(sock,token):

    #Montagem da mensagem em dicionario
    print("\n[STATUS] Realizando consulta de Status do Servidor...")    
    msg = {
        "tipo":     "operacao",
        "operacao": "historico",
        "token":    token
    #tipos: "autenticar", "operacao", "info", "logout"
    #operacao: "echo" "soma" "timestamp" "status" "historico"
    #parametros: "mensagem": "numeros":
    }

    #Transforma converte e envia a mensagem
    msg = json.dumps(msg)+"\n"         #converte o dicionario python pra json
    try:
        sock.sendall(msg.encode())         #encode - transforma em bytes pro socket enviar
        resposta = sock.recv(4096).decode()#recebimento da msg do servidor
    except Exception as e:
        print(f"[HISTORICO] Erro no servidor:", {e})
        return
    
    #################################
    #Print da mensagem montada DEBUG
    print(msg)           
    #Print da mensagem recebida DEBUG
    print("Resposta:", resposta )
    #################################

    ##=================== Tratamento da resposta ==================
    resposta = json.loads(resposta)

    if resposta.get("sucesso","") is True:

        historico = resposta.get("resultado", "").get("historico", [])
        print(f"[HISTORICO][✅] Consulta realizada com sucesso")
        for i, op in enumerate(historico, 1):
            sucesso = "✅" if op.get("sucesso") else "❌"
            print(f"{i}. Operação: {op.get('operacao')}, Status: {sucesso}, Timestamp: {op.get('timestamp')}")
    else:
        print(f"[HISTORICO][❌] Consulta falhou: ", resposta.get("mensagem",""))
    #=============================================================