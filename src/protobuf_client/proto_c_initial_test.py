import socket
from datetime import datetime
import sd_protocol_pb2 as proto

SERVER_IP = "3.88.99.255"
SERVER_PORT = 8082

# ---- Conectar ----
s = socket.socket()
s.connect((SERVER_IP, SERVER_PORT))

# ---- Criar requisição AUTH ----
req = proto.Requisicao()
req.auth.aluno_id = "385200"
req.auth.timestamp_cliente = datetime.now().isoformat()

# ---- Enviar ----
data = req.SerializeToString()
s.send(len(data).to_bytes(4, "big") + data)

# ---- Receber ----
tam = int.from_bytes(s.recv(4), "big")
resp = proto.Resposta()
resp.ParseFromString(s.recv(tam))

print(resp)
s.close()
