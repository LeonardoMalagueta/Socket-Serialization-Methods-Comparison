#ESTA OK ✅
import socket, json
from datetime import datetime

def soma_json(sock,token):
    print("\n[SOMA ➡️ ] Digite os numeros da operação, tecle x para terminar:")

    # Lê os números até o usuário digitar 'x'
    numeros = []
    while True:
        inp = input("> ").strip()
        if inp == "x":        # condição de parada se cumprir nao adiciona
            break
        numeros.append(inp)   # adiciona o numero na lista

    msg = {# A estrutura tem, dentro de tipo, as operações , e dentro de parametros tem que passar a mensagem
        "tipo":     "operacao",
        "operacao": "soma",
        "parametros": {"numeros": numeros},
        "token":    token
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
        print(f"[SOMA] Erro no servidor:", {e})
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
        print(f"[SOMA][✅] Operação realizada com sucesso")
        print(f"Numeros originais:  ",resposta.get("resultado").get("numeros_originais"))
        print(f"Soma dos numeros:   ",resposta.get("resultado").get("soma"))
        print(f"Média dos numeros:  ",resposta.get("resultado").get("media"))
        print(f"Máximo:             ",resposta.get("resultado").get("maximo"))
        print(f"Mínimo:             ",resposta.get("resultado").get("minimo"))
    else:
        print(f"[SOMA][❌] Operação falhou: ", resposta.get("mensagem",""))
    #=============================================================