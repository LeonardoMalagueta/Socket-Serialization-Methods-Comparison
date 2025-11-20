#ESTA OK ✅
import socket, json
from datetime import datetime

def logout_json(sock,matricula):
    print("\n[LOGOUT] Realizando logout no servidor...:")
    #Montagem da mensagem em dicionario
    msg = {
        "tipo": "logout",
        "aluno_id": matricula
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
        print(f"[Logout] Erro no servidor", {e})
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
        print(f"[AUTH][✅]:", resposta.get("mensagem",""))
    else:
        print("\n[LOGOUT ❌] Erro ao deslogar: ",resposta.get("mensagem",""))
    #=============================================================