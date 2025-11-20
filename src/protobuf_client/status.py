#ESTA OK ✅, recebendo resposta correta exceto o estatistica que vem do servidor vazio

import ast
import sd_protocol_pb2 as proto  #arquivo de conversao proto pra py

def status(detalhado, sock, token):
    #print("DETALHADO CHEGOU COM:", detalhado)
    print("\n[STATUS] Requisitando informações de tempo ao servidor...:")

    #montagem da requisicao soma (bloco padrao)
    req = proto.Requisicao()
    req.operacao.token = token
    req.operacao.operacao = "status"

    #serializacao e envio com correcao 4b  + data
    data = req.SerializeToString()                  #serializar a msg para dados binarios
    try:
        sock.send(len(data).to_bytes(4, "big") + data)  #envio

        #RECEBIMENTO
        tam = int.from_bytes(sock.recv(4), "big")
        resp = proto.Resposta()
        resp.ParseFromString(sock.recv(tam))
    except Exception as e:
        print(f"[STATUS] Erro no servidor:", {e})
        return

    # DEBUG TESTE RESPOSTA COMPLETA
    #print("\n[STATUS] resposta do servidor:")
    #print(resp)

    # Se for OK e pedido de detalhado, printa o detalhado, senao o normal e se n for ok o erro.
    modo = resp.WhichOneof("tipo")
    if modo == "ok":
        dados = resp.ok.dados
        if detalhado == "1": #Consulta completa

            #tratando a resposta de metricas como dicionario para imprimir separadamente
            metricas = dados["metricas"] 
            estatisticas = ast.literal_eval(metricas)

            print("\n[STATUS ✅] Consulta completa com sucesso, dados da operação:")
            print("[Status do servidor]:   ",dados.get("status", ""))
            print("CPU simulada:           ", estatisticas.get("cpu_simulado", ""))
            print("Memória simulada:       ", estatisticas.get("memoria_simulada", ""))
            print("Latência simulada:      ", estatisticas.get("latencia_simulada", ""))
        else: #Consulta simples
            print("\n[STATUS ✅] Consulta simples com sucesso, dados da operação:")
            print("[Status do servidor]:   ",dados.get("status", ""))


    elif modo == "erro":
        print("\n[STATUS ❌] Erro ao realizar consulta:", resp.erro.mensagem)
        print(resp.erro.mensagem)
    else:
         print("\n[STATUS ❌] Erro desconhecido.")