# 💬 Sala de Bate-Papo (Chat Room) com Interface Gráfica

Projeto de uma sala de bate-papo em Python, utilizando **sockets TCP** e interface gráfica com **Tkinter**. Suporta múltiplos usuários conectados simultaneamente e comunicação em tempo real.

---

## 🧩 Funcionalidades

- Comunicação síncrona entre até **10 clientes simultâneos**
- Interface gráfica usando **Tkinter**
- Mensagens enviadas e recebidas aparecem no chat
- Comandos especiais:
  - `exit` ou `quit`: desconecta do chat
  - `shutdown` (servidor): encerra o servidor com aviso de 10 segundos

---

## 🚀 Como Executar

### 1. Clone o projeto
```bash
git clone https://github.com/macedoflp/sala-de-bate-papo.git
cd sala-de-bate-papo
```

### 2. Execute o servidor
```bash
python server.py
```

### 3. Execute o cliente (interface gráfica)
```bash
python client.py
```

Você pode abrir quantas janelas quiser para simular múltiplos usuários.

---

## 🛠️ Requisitos

- Python 3.8+
- Bibliotecas padrão (`socket`, `threading`, `tkinter`)

---

## 📂 Arquivos

| Arquivo         | Descrição                                 |
|-----------------|-------------------------------------------|
| `server.py`     | Servidor que aceita conexões e transmite mensagens |
| `client.py` | Cliente com interface gráfica Tkinter     |