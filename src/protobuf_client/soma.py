#ESTA OK ✅, recebendo resposta correta e printando tudo corretamente

import sd_protocol_pb2 as proto  #arquivo de conversao proto pra py

def soma(sock, token):
    print("\n[SOMA ➡️ ] Digite os numeros da operação, tecle x para terminar:")

    # Lê os números até o usuário digitar 'x'
    numeros = []
    while True:
        inp = input("> ").strip()
        if inp == "x":        # condição de parada se cumprir nao adiciona
            break
        numeros.append(inp)   # adiciona o numero na lista

    #montagem da requisicao soma (bloco padrao)
    req = proto.Requisicao()
    req.operacao.token = token
    req.operacao.operacao = "soma"
    data = numeros

    # adiciona cada número como num0, num1, num2...
    for i, n in enumerate(numeros):
        req.operacao.parametros["numeros"] = ",".join(numeros)


    #serializacao e envio com correcao 4b  + data
    data = req.SerializeToString()                  #serializar a msg para dados binarios
    try:
        sock.send(len(data).to_bytes(4, "big") + data)  #envio
        #RECEBIMENTO
        tam = int.from_bytes(sock.recv(4), "big")
        resp = proto.Resposta()
        resp.ParseFromString(sock.recv(tam))
    except Exception as e:
        print(f"[SOMA] Erro no servidor:", {e})
        return

    # DEBUG TESTE RESPOSTA COMPLETA
    #print("\n[SOMA] resposta do servidor:")
    #print(resp)

    # Se for OK, mostrar formatadinho
    modo = resp.WhichOneof("tipo")
    if modo == "ok":
        dados = resp.ok.dados

        print("\n[SOMA ✅] Soma realizada com sucesso, dados da operação:")
        print("[Soma]                ", dados.get("soma", ""))
        print("[Media]               ", dados.get("media", ""))
        print("[Maximo]              ", dados.get("maximo", ""))
        print("[Minimo]              ", dados.get("minimo", ""))
        print("[Numeros processador] ", dados.get("numeros_originais", ""))

        #print("[Timestamp Calculo]", dados.get("timestamp_calculo", ""))

    elif modo == "erro":
        print("\n[SOMA ❌] Erro ao realizar a operação: ", resp.erro.mensagem)
        print(resp.erro.mensagem)
    else:
        print("[AUTH][❌] Erro desconhecido")
