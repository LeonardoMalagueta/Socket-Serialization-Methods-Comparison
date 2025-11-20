#ESTA OK ✅

import socket
from datetime import datetime

def soma_string(sock,token):
    print("\n[SOMA ➡️ ] Digite os numeros da operação, tecle x para terminar:")
    numeros = []
    while True:
        inp = input("> ").strip()
        if inp == "x":        # condição de parada se cumprir nao adiciona
            break
        numeros.append(inp)   # adiciona o numero na lista
    numeros_str = ",".join(str(n) for n in numeros)

   
    #============= Montagem da mensagem STRING =================
    timestamp = datetime.now().isoformat()
    msg = f"OP|operacao=soma|nums={numeros_str}|token={token}|timestamp={timestamp}|FIM"
    msg = (msg+"\n").encode("utf-8")

    #MODELO: OP|operacao=echo|mensagem=msg,msg,msg,msg|token={token}|timestamp={timestamp}|FIM
    #para o soma é nums = numeros separados por virgula
    #Separadores: pipe (|) entre campos
    #Finaliza simpre as msg com |FIM
    #Codificação UTF-8
    #Terminador:\n
    #===========================================================

    #send no socket
    try:
        sock.sendall(msg)

        resposta = sock.recv(4096).decode("utf-8").strip()
        resposta_debug = resposta
    except Exception as e:
        print(f"[LOGOUT] Erro no servidor:", {e})
        return

    if resposta.endswith("|FIM"):
        resposta = resposta[:-4]

    #rasgar resposta em pedaços e montar o dicionario ------
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


    ##################################
    ##Print da mensagem montada DEBUG
    #print(msg)           
    ##Print da mensagem recebida DEBUG
    #print(resposta_debug)
    ##################################
    
#
    ##=================== Tratamento da resposta ==================
    if dados.get("sucesso","") is True:
        print(f"[SOMA][✅] Operação realizada com sucesso")
        print(f"Soma dos numeros:   ",dados.get("soma", ""))
        print(f"Média:              ",dados.get("media", ""))
        print(f"Máximo:             ",dados.get("maximo", ""))
        print(f"Mínimo:             ",dados.get("minimo", ""))
        print(f"Numeros processados:",dados.get("numeros_originais", ""))
    elif dados.get("sucesso", "") is False:
        print("[SOMA][❌] Erro ao autenticar: ", dados.get("msg",""))
    else:
        print("[SOMA][❌] Erro desconhecido.")
