import socket
from datetime import datetime

SERVER_IP = "3.88.99.255"
SERVER_PORT = 8080

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((SERVER_IP, SERVER_PORT))

def enviar_mensagem(msg):
    cliente.sendall((msg + "\n").encode("utf-8"))
    resposta = cliente.recv(4096).decode("utf-8").strip()
    print("Servidor respondeu:", resposta)

matricula = "385200"
timestamp = datetime.now().isoformat()
msg_auth = f"AUTH|aluno_id={matricula}|timestamp={timestamp}|FIM"

enviar_mensagem(msg_auth)
