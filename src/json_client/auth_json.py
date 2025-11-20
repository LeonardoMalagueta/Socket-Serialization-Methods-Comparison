#ESTA OK ✅
import socket, json
from datetime import datetime

def auth_json(sock,matricula):
    sock.settimeout(10)
    #Montagem da mensagem em dicionario
    msg = {
        "tipo": "autenticar",
        "aluno_id": matricula
    #tipos: "autenticar", "operacao", "info", "logout"
    #operacao: "echo" "soma"
    #parametros: "mensagem" "numeros"
    }

    #Transforma converte e envia a mensagem
    msg = json.dumps(msg)+"\n"         #converte o dicionario python pra json
    
    try:
        sock.sendall(msg.encode())         #encode - transforma em bytes pro socket enviar
        resposta = sock.recv(4096).decode()#recebimento da msg do servidor
    except Exception as e:
        print(f"[AUTH] Erro no servidor:", {e})
        return

    #################################
    #Print da mensagem montada DEBUG
    #print(msg)           
    #Print da mensagem recebida DEBUG
    #print("Resposta:", resposta )
    #################################

    #=================== Tratamento da resposta ==================
    resposta = json.loads(resposta)
    if resposta.get("sucesso","") is True:
        print(f"[AUTH][✅] Autenticação realizada com sucesso")
        token = resposta.get("token", "")
        nome  = resposta.get("dados_aluno", {}).get("nome", "") #no jason o nome esta dentro de "nome" dentro de "dados"
        return token, nome
    else:
        print(f"[AUTH][❌] Autenticação falhou")
    #=============================================================