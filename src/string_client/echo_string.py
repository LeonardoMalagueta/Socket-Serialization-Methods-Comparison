#ESTA OK ✅

import socket
from datetime import datetime

def echo_string(sock,token):
    print("\n[ECHO ➡️ ] Digite a mensagem para o ECHO:")
    msg = input("> ").strip()
   
    #============= Montagem da mensagem STRING =================
    timestamp = datetime.now().isoformat()
    msg = f"OP|operacao=echo|mensagem={msg}|token={token}|timestamp={timestamp}|FIM"
    msg = (msg+"\n").encode("utf-8")

    #MODELO: OP|operacao=echo|mensagem={msg}|token={token}|timestamp={timestamp}|FIM
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
        print(f"[LOGOUT] Erro no servidor:", {e})
        return


    #print(resposta) #DEBUG ☺
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
    ##print(msg)           
    ##Print da mensagem recebida DEBUG
    ##print(resposta)
    ##################################
    
#
    ##=================== Tratamento da resposta ==================
    if dados.get("sucesso","") is True:
        print(f"[ECHO][✅] Operação realizada com sucesso, resposta:")
        print(f"Mensagem origianl:      ",dados.get("mensagem_original", ""))
        print(f"ECHO da mensagem:       ",dados.get("mensagem_eco", ""))
        print(f"Timestamp do servidor:  ",dados.get("timestamp_servidor", ""))
        print(f"Tamanho da mensagem:    ",dados.get("tamanho_mensagem", ""), " caracteres")
        print(f"Hash MD5:               ",dados.get("hash_md5", ""))
    elif dados.get("sucesso", "") is False:
        print("[ECHO][❌] Erro ao autenticar: ", dados.get("msg",""))
    else:
        print("[ECHO][❌] Erro desconhecido.")
