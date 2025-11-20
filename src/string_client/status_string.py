#ESTA OK ✅

import ast
import socket
from datetime import datetime

def status_string(detalhado,sock,token):
    print("\n[STATUS] Requisitando informações status do servidor...")
    #============= Montagem da mensagem STRING =================
    timestamp = datetime.now().isoformat()
    msg = f"OP|operacao=status|token={token}|timestamp={timestamp}|FIM"
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

    metricas_raw = dados.get("metricas", "{}")
    metricas = ast.literal_eval(metricas_raw)



    ##################################
    ##Print da mensagem montada DEBUG
    #print(msg)           
    ##Print da mensagem recebida DEBUG
    #print(resposta_debug)
    ##################################
    
#
    #=================== Tratamento da resposta ==================
    if dados.get("sucesso","") is True:
        if detalhado == "1":
            print(f"[STATUS][✅] Consulta realizada com sucesso, resposta:")
            print(f"Status do servidor:     ",dados.get("status", ""))
            print(f"Operações processadas:  ",dados.get("operacoes_processadas", ""))
            print(f"Sessões ativas:         ",dados.get("sessoes_ativas", ""))
            print(f"Tempo de atividade:     ",dados.get("tempo_ativo", ""))
            print(f"Versão do servidor:     ",dados.get("versao", ""))
            print(f"CPU's simuladas:        ",metricas.get("cpu_simulado", ""))
            print(f"Memória simulada:       ",metricas.get("memoria_simulada", ""))
            print(f"Latência simulada:      ",metricas.get("latencia_simulada", ""))
        else:
            print(f"[STATUS][✅] Consulta realizada com sucesso, resposta:")
            print(f"Status do servidor:     ",dados.get("status", ""))
            print(f"Operações processadas:  ",dados.get("operacoes_processadas", ""))
    elif dados.get("sucesso", "") is False:
        print("[STATUS][❌] Erro ao autenticar: ", dados.get("msg",""))
    else:
        print("[STATUS][❌] Erro desconhecido.")
