#ESTA OK ✅, recebendo resposta correta e retornando a chave que funciona

import sd_protocol_pb2 as proto     # o arquivo de conversao protocolbuf pra python
from datetime import datetime       # pra usar o timestamp

def auth(sock, aluno_id):
    req = proto.Requisicao()
    req.auth.aluno_id = aluno_id    # matricula
    req.auth.timestamp_cliente = datetime.now().isoformat()

    #serializa e envia com aquela correcao dos 4bit de tamanho + os dados
    data = req.SerializeToString()
    
    try:
        sock.send(len(data).to_bytes(4, "big") + data)
        #tamanho e conteudo com os 4 bit iniciais
        tam = int.from_bytes(sock.recv(4), "big")
        resp = proto.Resposta()
        resp.ParseFromString(sock.recv(tam))
    except Exception as e:
        print(f"[AUTH] Erro no servidor:", {e})
        return
    
    


    #debug de exibicao da resposta
    #print("\n[AUTH] resposta do servidor:")
    #print(resp)

    # Extrai só o token da resposta OK do servidor se ela tiver sido ok

    modo = resp.WhichOneof("tipo")
    if modo == "ok":
        token = resp.ok.dados["token"]
        nome = resp.ok.dados["nome"]
        #print("[token recebido]")
        #print(token)
        return token , nome
    elif modo == "erro":
        print("[AUTH][❌] Erro ao autenticar: ", resp.erro.mensagem)
        return None
    else:
        print("[AUTH][❌] Erro desconhecido.")