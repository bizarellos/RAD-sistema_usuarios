from telas.utils_gui import limpar_janela
import tkinter as tk
from tkinter import messagebox
import telas.cadastro
import telas.recuperar_senha
import telas.crud_usuarios
from database import get_user_by_email
from utils import verify_password

def abrir_tela_login(root):
    limpar_janela(root)

    tk.Label(root, text="Login").pack()
    tk.Label(root, text="Email").pack()
    email = tk.Entry(root)
    email.pack()

    tk.Label(root, text="Senha").pack()
    senha = tk.Entry(root, show="*")
    senha.pack()

    def autenticar():
        user = get_user_by_email(email.get())
        if user and verify_password(senha.get(), user[3].encode()):
            messagebox.showinfo("Sucesso", "Login efetuado com sucesso!")
            telas.crud_usuarios.abrir_tela_crud(root)
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    tk.Button(root, text="Login", command=autenticar).pack()
    tk.Button(root, text="Esqueci minha senha", command=lambda: telas.recuperar_senha.abrir_tela_recuperar(root)).pack()
    tk.Button(root, text="Criar Usuário", command=lambda: telas.cadastro.abrir_tela_cadastro(root)).pack()

def limpar_janela(root):
    for widget in root.winfo_children():
        widget.destroy()