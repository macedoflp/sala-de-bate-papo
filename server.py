# server.py
import socket
import threading
import time

HOST = 'localhost'
PORT = 12345

clients = []
usernames = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[Servidor iniciado] Aguardando conexões em {HOST}:{PORT}...")

def broadcast(msg, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(msg.encode())
            except:
                client.close()
                clients.remove(client)

def handle_client(client):
    try:
        client.send("Digite seu nome de usuário: ".encode())
        username = client.recv(1024).decode().strip()
        usernames[client] = username
        clients.append(client)
        broadcast(f"[Sistema] {username} entrou na sala.", client)
        print(f"[Conectado] {username} conectado.")

        while True:
            msg = client.recv(1024).decode()
            if msg.lower() in ['exit', 'quit']:
                broadcast(f"[Sistema] {username} saiu da sala.", client)
                print(f"[Desconectado] {username} desconectado.")
                clients.remove(client)
                client.close()
                break
            else:
                broadcast(f"{username}: {msg}", client)
    except:
        if client in clients:
            clients.remove(client)
        print(f"[Erro] Conexão com {usernames.get(client, 'desconhecido')} encerrada.")
        client.close()

def admin_commands():
    while True:
        cmd = input()
        if cmd.strip() == 'shutdown':
            broadcast("[Sistema] Servidor será desligado em 10 segundos.")
            time.sleep(10)
            for client in clients:
                client.close()
            server.close()
            print("[Servidor encerrado]")
            break

threading.Thread(target=admin_commands, daemon=True).start()

while True:
    try:
        client, addr = server.accept()
        if len(clients) >= 10:
            client.send("Sala cheia. Tente mais tarde.".encode())
            client.close()
            continue
        thread = threading.Thread(target=handle_client, args=(client,), daemon=True)
        thread.start()
    except:
        break
