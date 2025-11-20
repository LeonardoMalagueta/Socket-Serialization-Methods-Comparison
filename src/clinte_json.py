import socket, json
from datetime import datetime

ip = "3.88.99.255"
porta = 8081


#============================== Conectar ====================================
try:
    s = socket.socket()
    s.connect((ip, porta))
    print(f"✅ Conexao com {ip}:{porta} JSON SERVER bem sucedida")
except Exception as e:
    print(f"❌ Erro ao conectar no servdor de JSON: {e}")
#============================================================================


#mensagem a ser enviada
msg = {
    "tipo": "autenticar",
    "aluno_id": "385200"
}


#====================== Transforma converte e envia a mensagem ==============
msg = json.dumps(msg)+"\n"                      #converte o dicionario python pra json
print(msg)
s.sendall(msg.encode())                         #encode - transforma em bytes pro socket enviar

resposta = s.recv(4096).decode()
#print("Resposta:", resposta )
#============================================================================


#=================== Tratando o Json como dicionario python ==================
resposta = json.loads(resposta)
if "token" in resposta:
    token = resposta["token"]
    print("✅ Token de confirmacao recebido: " + token)
else:
    print(f"❌ Token não encontrado na resposta")
#============================================================================

s.close()   