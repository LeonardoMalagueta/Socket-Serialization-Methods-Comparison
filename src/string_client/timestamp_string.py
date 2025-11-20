#ESTA OK ✅

import socket
from datetime import datetime

def timestamp_string(sock,token):
    print("\n[TIMESTAMP] Requisitando informações de tempo ao servidor...")
    #============= Montagem da mensagem STRING =================
    timestamp = datetime.now().isoformat()
    msg = f"OP|operacao=timestamp|token={token}|timestamp={timestamp}|FIM"
    msg_utf8 = (msg+"\n").encode("utf-8")

    #MODELO: OP|operacao=echo|mensagem={msg}|token={token}|timestamp={timestamp}|FIM
    #Separadores: pipe (|) entre campos
    #Finaliza simpre as msg com |FIM
    #Codificação UTF-8
    #Terminador:\n
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
    ##=================== Tratamento da resposta ==================
    if dados.get("sucesso","") is True:
        print(f"[TIMESTAMP][✅] Consulta realizada com sucesso, resposta:")
        print(f"Timestamp do servidor:  ",dados.get("timestamp_formatado", ""))
        print(f"Microsegundos:          ",dados.get("microsegundo", ""))
        print(f"Timestamp em Unix:      ",dados.get("timestamp_unix", ""))
        print(f"Timestamp em ISO:       ",dados.get("timestamp_iso", ""))
    elif dados.get("sucesso", "") is False:
        print("[TIMESTAMP][❌] Erro ao autenticar: ", dados.get("msg",""))
    else:
        print("[TIMESTAMP][❌] Erro desconhecido.")
