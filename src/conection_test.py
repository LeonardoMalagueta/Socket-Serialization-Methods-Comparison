import socket

SERVER_IP = "3.88.99.255"
P1 = 8080
P2 = 8081
P3 = 8082

try:
    s = socket.socket()
    s.settimeout(2)
    s.connect((SERVER_IP, P1))
    print(f"✅ Servidor de STRING online {P1}")
    s.close()
except Exception as e:
        print(f"❌ Servidor de STRING nao responde: {e}")

try:
    s = socket.socket()
    s.settimeout(2)
    s.connect((SERVER_IP, P2))
    print(f"✅ Servidor de JSON online {P2}")
    s.close()
except Exception as e:
        print(f"❌ Servidor de JSON nao responde: {e}")

try:
    s = socket.socket()
    s.settimeout(2)
    s.connect((SERVER_IP, P3))
    print(f"✅ Servidor de PROTOBUF online {P3}")
    s.close()
except Exception as e:
        print(f"❌ Servidor de PROTOBUF nao responde: {e}")

print(f"\n Prima a telca ENTER para fechar...")
input("> ").strip()
