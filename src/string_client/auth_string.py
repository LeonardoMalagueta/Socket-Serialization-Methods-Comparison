#ESTA OK ✅

import socket, json
from datetime import datetime

def auth_string(sock,matricula):
    print(f"[AUTH] Autenticando acesso...")
    
   
    #============= Montagem da mensagem STRING =================
    timestamp = datetime.now().isoformat()
    msg = f"AUTH|aluno_id={matricula}|timestamp={timestamp}|FIM"
    msg = (msg+"\n").encode("utf-8")
    #Separadores: pipe (|) entre campos
    #Finaliza simpre as msg com |FIM
    #Codificação UTF-8
    #Terminador:\n 
    #===========================================================

    #send no socket
    try:
        sock.sendall(msg)
        resposta = sock.recv(4096).decode("utf-8").strip()
    except Exception as e:
        print(f"[AUTH] Erro no servidor:", {e})
        return

    if resposta.endswith("|FIM"):
        resposta = resposta[:-4]


    #rasgas resposta em pedaços e montar o dicionario ------
    campos = resposta.split("|")
    dados = {}
    for campo in campos:
        if "=" in campo:
            chave, valor = campo.split("=", 1)
            dados[chave] = valor
            #print(chave, valor)
        elif campo == "OK":
            dados["sucesso"] = True
        else:
            dados["sucesso"] = False
    #-----------------------------------------------------

    ##################################
    ##Print da mensagem montada DEBUG
    ##print(msg)           
    ##Print da mensagem recebida DEBUG
    ##print(resposta)
    ##################################
    
#
    ##=================== Tratamento da resposta =================
    if dados.get("sucesso","") is True:
        token = dados.get("token", "")
        nome  = dados.get("nome","")
        return token, nome
    elif dados.get("sucesso", "") is False:
        print("[AUTH][❌] Erro ao autenticar: ", dados.get("msg",""))
    else:
        print("[AUTH][❌] Erro desconhecido.")
