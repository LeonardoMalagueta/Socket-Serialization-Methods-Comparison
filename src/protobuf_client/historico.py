#ESTA OK ✅


import sd_protocol_pb2 as proto  #arquivo de conversao proto pra py
import ast

def historico(sock, token):
    print("\n[HISTORICO] Historico de operações usuário:")
    #montagem da requisicao echo
    req = proto.Requisicao()
    req.operacao.token = token
    req.operacao.operacao = "historico"

    #serializacao e envio com correcao 4b  + data
    data = req.SerializeToString()
    try:
        sock.send(len(data).to_bytes(4, "big") + data)
        #RECEBIMENTO
        tam = int.from_bytes(sock.recv(4), "big")
        resp = proto.Resposta()
        resp.ParseFromString(sock.recv(tam))
    except Exception as e:
        print(f"[HISTORICO] Erro no servidor:", {e})
        return

    # DEBUG TESTE RESPOSTA COMPLETA
    print("\n[HISTORICO] resposta do servidor:")
    print(resp)


    # Se for OK, mostrar formatadinho
    modo = resp.WhichOneof("tipo")

    if modo == "ok":
        dados = resp.ok.dados
        print("\n[HISTORICO ✅] Consulta realizada com sucesso, resultados:")

        historico = dados.get("historico")
        historico = ast.literal_eval(historico)
        for i, op in enumerate(historico, 1):
            print("entrou")
            sucesso = "✅" if op.get("sucesso") else "❌"
            print(f"{i}. Operação: {op.get('operacao')}, Status: {sucesso}, Timestamp: {op.get('timestamp')}")
        print("[Original] ", dados.get("mensagem_original", ""))
    
    elif modo == "erro":
        print("\n[HISTORICO ❌] Erro ao realizar a operação: ", resp.erro.mensagem)
    else:
        print("\n[HISTORICO ❌] Erro desconhecido.")
