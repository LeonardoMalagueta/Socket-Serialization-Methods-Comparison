#ESTA OK ✅

import ast
import socket
from datetime import datetime

def logout_string(sock,token):
    print("\n[LOGOUT] Realizando logout no servidor...:")
    
    #============= Montagem da mensagem STRING =================
    timestamp = datetime.now().isoformat()
    msg = f"LOGOUT|token={token}|timestamp={timestamp}|FIM"
    msg_utf8 = (msg+"\n").encode("utf-8")
    #===========================================================

    #send no socket
    try:
        sock.sendall(msg_utf8)
        resposta = sock.recv(4096).decode("utf-8").strip()
        resposta_debug = resposta
    except Exception as e:
        print(f"[LOGOUT] Erro no servidor:", {e})
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
            #print(chave, valor) #DEBUG ☺
        elif campo == "OK":
            dados["sucesso"] = True
        else:
            dados["sucesso"] = False
    #-----------------------------------------------------

    ##################################
    ##Print da mensagem montada DEBUG
    #print(msg)           
    ##Print da mensagem recebida DEBUG
    #print(resposta_debug)
    ##################################
    
#
    #=================== Tratamento da resposta ==================
    if dados.get("sucesso","") is True:
        print(f"[LOGOUT][✅]", dados.get("msg",""))
    elif dados.get("sucesso", "") is False:
        print("[LOGOUT][❌] Erro ao deslogar: ", dados.get("msg",""))
    else:
        print("[LOGOUT][❌] Erro desconhecido.")