#ESTA OK ✅, recebendo resposta correta e retornando o echo


import sd_protocol_pb2 as proto  #arquivo de conversao proto pra py

def echo(sock, token):
    print("\n[ECHO ➡️ ] Digite a mensagem para o ECHO:")
    msg = input("> ").strip()

    #montagem da requisicao echo
    req = proto.Requisicao()
    req.operacao.token = token
    req.operacao.operacao = "echo"
    req.operacao.parametros["mensagem"] = msg

    #serializacao e envio com correcao 4b  + data
    data = req.SerializeToString()
    try:
        sock.send(len(data).to_bytes(4, "big") + data)
        #RECEBIMENTO
        tam = int.from_bytes(sock.recv(4), "big")
        resp = proto.Resposta()
        resp.ParseFromString(sock.recv(tam))
    except Exception as e:
        print(f"[ECHO] Erro no servidor:", {e})
        return
    # DEBUG TESTE RESPOSTA COMPLETA
    #print("\n[ECHO] resposta do servidor:")
    #print(resp)

    # Se for OK, mostrar formatadinho
    modo = resp.WhichOneof("tipo")
    if modo == "ok":
        dados = resp.ok.dados
        print("\n[ECHO ✅] Echo realizado com sucesso, resultados:")
        print("[Original] ", dados.get("mensagem_original", ""))
        print("[Echo]       ", dados.get("mensagem_eco", ""))
        print("[Tamanho]    ", dados.get("tamanho_mensagem", ""))
        print("[Hash MD5]   ", dados.get("hash_md5", "")) 
        print("[Timestamp]  ", dados.get("timestamp_servidor", ""))

    elif modo == "erro":
        print("\n[ECHO ❌] Erro ao realizar a operação: ", resp.erro.mensagem)
    else:
        print("\n[ECHO ❌] Erro desconhecido.")
    