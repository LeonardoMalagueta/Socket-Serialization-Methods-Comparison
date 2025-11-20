#ESTA OK ✅
import socket, json
from datetime import datetime

def echo_json(sock,token):
    #Montagem da mensagem em dicionario

    print("\n[ECHO ➡️ ] Digite a mensagem para o ECHO:")
    texto = input("> ").strip()
    texto = texto

    
    msg = {
        "tipo":         "operacao",
        "operacao":     "echo",
        "parametros":   {"mensagem": texto},
        "token":        token
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
        print(f"[ECHO] Erro no servidor:", {e})
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
        print(f"[ECHO][✅] Operação realizada com sucesso")
        print(f"Mensagem origianl:      ",resposta.get("resultado").get("mensagem_original"))
        print(f"ECO da mensagem:        ",resposta.get("resultado").get("mensagem_eco"))
        print(f"tamanho da mensagem:    ",resposta.get("resultado").get("tamanho_mensagem"))
        print(f"Hash MD5 da resposta:   ",resposta.get("resultado").get("hash_md5"))
        print(f"Timestamp da resposta:  ",resposta.get("resultado").get("timestamp_servidor"))
    else:
        print(f"[ECHO][❌] Operação falhou: ", resposta.get("mensagem",""))
    #=============================================================