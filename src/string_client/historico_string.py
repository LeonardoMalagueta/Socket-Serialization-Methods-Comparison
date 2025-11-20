#ESTA OK ✅

import ast
import socket
from datetime import datetime

def historico_string(sock,token):

    print("\n[HISTORICO] Realizando consulta de historico do Servidor...")  

    #============= Montagem da mensagem STRING =================
    timestamp = datetime.now().isoformat()
    msg = f"OP|operacao=historico|token={token}|timestamp={timestamp}|FIM"
    msg_utf8 = (msg+"\n").encode("utf-8")
    #===========================================================

    #send no socket
    try:
        sock.sendall(msg_utf8)
        resposta = sock.recv(4096).decode("utf-8").strip()
    except Exception as e:
        print(f"[LOGOUT] Erro no servidor:", {e})
        return
    #resposta_debug = resposta

    if resposta.endswith("|FIM"):
        resposta = resposta[:-4]
    #rasgas resposta em pedaços e montar o dicionario ------
    campos = resposta.split("|")
    dados = {}
    for campo in campos:
        if "=" in campo:
            chave, valor = campo.split("=", 1)
            dados[chave] = valor
        elif campo == "OK":
            dados["sucesso"] = True
        else:
            dados["sucesso"] = False
    #-----------------------------------------------------

    historico_raw = dados.get("historico", "{}")
    historico_corrigido = "[" + historico_raw + "]"
    historico = ast.literal_eval(historico_corrigido)


    ##################################
    ##Print da mensagem montada DEBUG
    #print(msg)           
    ##Print da mensagem recebida DEBUG
    #print(resposta_debug)
    ##################################
    
#
    #=================== Tratamento da resposta ==================
    if dados.get("sucesso","") is True:
        print(f"[HISTORICO][✅] Consulta realizada com sucesso")
        for i, op in enumerate(historico, 1):
            sucesso = "✅" if op.get("sucesso") else "❌"
            print(f"{i}. Operação: {op.get('operacao')}, Status: {sucesso}, Timestamp: {op.get('timestamp')}")
    elif dados.get("sucesso", "") is False:
        print("[HISTORICO][❌] Erro ao consultar histórico: ", dados.get("msg",""))
    else:
        print("[HISTORICO][❌] Erro desconhecido.")