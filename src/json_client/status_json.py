#ESTA OK ✅
import socket, json
from datetime import datetime

def status_json(detalhado,sock,token):

    #Montagem da mensagem em dicionario
    print("\n[STATUS] Realizando consulta de Status do Servidor:")    
    msg = {
        "tipo":     "operacao",
        "operacao": "status",
        "token":    token
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
        print(f"[STATUS] Erro no servidor:", {e})
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
        print(f"[STATUS][✅] Consulta realizada com sucesso, STATUS do servidor:")
        if detalhado == "1":
            print(f"Status:             ",resposta.get("resultado").get("status"))
            print(f"Sessões ativas:     ",resposta.get("resultado").get("sessoes_ativas"))
            print(f"Tempo de atividade: ",resposta.get("resultado").get("tempo_ativo"))
            print(f"Versão:             ",resposta.get("resultado").get("versao"))
            print(f"OP's processadas:   ",resposta.get("resultado").get("operacoes_processadas"))
            print(f"CPU's simuladas:    ",resposta.get("resultado").get("metricas").get("cpu_simulado"))
            print(f"Memória simulada:   ",resposta.get("resultado").get("metricas").get("memoria_simulada"))
            print(f"Latência simulada:  ",resposta.get("resultado").get("metricas").get("latencia_simulada"))
        else:
            print(f"Status:             ",resposta.get("resultado").get("status"))
            print(f"OP's processadas:   ",resposta.get("resultado").get("operacoes_processadas"))
    else:
        print(f"[STATUS][❌] Consulta falhou: ", resposta.get("mensagem",""))
    #=============================================================