# client_gui.py
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox

HOST = 'localhost'
PORT = 12345

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Sala de Bate-Papo")

        self.chat_label = tk.Label(master, text="Chat:")
        self.chat_label.pack(padx=10, pady=5)

        self.text_area = scrolledtext.ScrolledText(master)
        self.text_area.pack(padx=10, pady=5)
        self.text_area.config(state='disabled')

        self.msg_entry = tk.Entry(master)
        self.msg_entry.pack(padx=10, pady=5, fill=tk.X)
        self.msg_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Enviar", command=self.send_message)
        self.send_button.pack(padx=10, pady=5)

        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = simpledialog.askstring("Usuário", "Digite seu nome de usuário:", parent=master)

        try:
            self.client.connect((HOST, PORT))
            threading.Thread(target=self.receive_messages, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível conectar ao servidor: {e}")
            master.quit()
            return

    def receive_messages(self):
        try:
            self.client.send(self.username.encode())
            while True:
                msg = self.client.recv(1024).decode()
                if msg:
                    self.text_area.config(state='normal')
                    self.text_area.insert(tk.END, msg + '\n')
                    self.text_area.yview(tk.END)
                    self.text_area.config(state='disabled')
                else:
                    break
        except:
            self.client.close()

    def send_message(self, event=None):
        msg = self.msg_entry.get()
        if msg:
            try:
                self.client.send(msg.encode())
                self.text_area.config(state='normal')
                self.text_area.insert(tk.END, f"{self.username}: {msg}\n")
                self.text_area.yview(tk.END)
                self.text_area.config(state='disabled')
                if msg.lower() in ['exit', 'quit']:
                    self.master.quit()
            except:
                messagebox.showerror("Erro", "Erro ao enviar mensagem.")
            self.msg_entry.delete(0, tk.END)

    def on_close(self):
        try:
            self.client.send("exit".encode())
        except:
            pass
        self.client.close()
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    client_gui = ChatClient(root)
    root.mainloop()
