#ESTA OK ✅, recebendo resposta correta
import sd_protocol_pb2 as proto  #arquivo de conversao proto pra py

def logout(sock, token):
    print("\n[LOGOUT] Realizando logout no servidor...:")

    #montagem da requisicao soma (bloco padrao)
    req = proto.Requisicao()
    req.logout.token = token

    #serializacao e envio com correcao 4b  + data
    data = req.SerializeToString()                  #serializar a msg para dados binarios
    try:
        sock.send(len(data).to_bytes(4, "big") + data)  #envio
        #RECEBIMENTO
        tam = int.from_bytes(sock.recv(4), "big")
        resp = proto.Resposta()
        resp.ParseFromString(sock.recv(tam))
    except Exception as e:
        print(f"[LOGOUT] Erro no servidor:", {e})
        return

    # DEBUG TESTE RESPOSTA COMPLETA
    #print("\n[LOGOUT] Resposta do servidor:")
    #print(resp)

    # Se for OK e pedido de detalhado, printa o detalhado, senao o normal e se n for ok o erro.
    modo = resp.WhichOneof("tipo")

    if modo == "ok":
        dados = resp.ok.dados
        print("\n[LOGOUT ✅]Resposta do servidor: ", dados.get("msg",""))
    elif modo == "erro":
        print("\n[LOGOUT ❌] Erro ao realizar a operação: ", resp.erro.mensagem)
    else:
        print("\n[LOGOUT ❌] Erro desconhecido")
