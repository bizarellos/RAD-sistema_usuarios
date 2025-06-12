from telas.utils_gui import limpar_janela
import tkinter as tk
from tkinter import messagebox
from database import create_user
from utils import hash_password
import telas.login

def abrir_tela_cadastro(root):
    limpar_janela(root)

    tk.Label(root, text="Cadastro de Usuário").pack()
    tk.Label(root, text="Nome").pack()
    nome = tk.Entry(root)
    nome.pack()

    tk.Label(root, text="Email").pack()
    email = tk.Entry(root)
    email.pack()

    tk.Label(root, text="Senha").pack()
    senha = tk.Entry(root, show="*")
    senha.pack()

    def salvar():
        if not nome.get() or not email.get() or not senha.get():
            messagebox.showwarning("Erro", "Todos os campos são obrigatórios.")
            return
        try:
            hashed = hash_password(senha.get())
            create_user(nome.get(), email.get(), hashed)
            messagebox.showinfo("Sucesso", "Usuário criado com sucesso.")
            telas.login.abrir_tela_login(root)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar usuário: {str(e)}")

    tk.Button(root, text="Salvar", command=salvar).pack()
    tk.Button(root, text="Voltar", command=lambda: telas.login.abrir_tela_login(root)).pack()

def limpar_janela(root):
    for widget in root.winfo_children():
        widget.destroy()