#ESTA OK ✅, recebendo resposta correta e printando tudo direitinho

import sd_protocol_pb2 as proto  #arquivo de conversao proto pra py

def timestamp(sock, token):
    print("\n[TIMESTAMP] Requisitando informações de tempo ao servidor...:")

    #montagem da requisicao soma (bloco padrao)
    req = proto.Requisicao()
    req.operacao.token = token
    req.operacao.operacao = "timestamp"

    #serializacao e envio com correcao 4b  + data
    data = req.SerializeToString()                  #serializar a msg para dados binarios
    try:
        sock.send(len(data).to_bytes(4, "big") + data)  #envio

        #RECEBIMENTO
        tam = int.from_bytes(sock.recv(4), "big")
        resp = proto.Resposta()
        resp.ParseFromString(sock.recv(tam))
    except Exception as e:
        print(f"[TIMESTAMP] Erro no servidor:", {e})
        return

    # DEBUG TESTE RESPOSTA COMPLETA
    #print("\n[TIMESTAMP] resposta do servidor:")
    #print(resp)

    # Se for OK, mostrar formatadinho
    modo = resp.WhichOneof("tipo")

    if modo == "ok":
        dados = resp.ok.dados
        print("\n[TIMESTAMP ✅] Consulta realizada com sucesso, dados da operação:")
        print("[Tempo do servidor]:   ",dados.get("timestamp_formatado", ""))
        print("[Microsegundos]:       ",dados.get("microsegundo", ""))
        #❌❌❌servidor não possui informações de fuso horario❌❌❌.

    elif modo == "erro":
        print("\n[TIMESTAMP ❌] Erro ao realizar a operação: ", resp.erro.mensagem)
        
    else:
        print("\n[TIMESTAMP ❌] Erro desconhecido")