from telas.utils_gui import limpar_janela
import tkinter as tk
from tkinter import messagebox
import telas.login

def abrir_tela_recuperar(root):
    limpar_janela(root)

    tk.Label(root, text="Recuperar Senha").pack()
    tk.Label(root, text="Email cadastrado").pack()
    email = tk.Entry(root)
    email.pack()

    def enviar():
        messagebox.showinfo("Recuperação", f"Email enviado para {email.get()} (simulação).")
        telas.login.abrir_tela_login(root)

    tk.Button(root, text="Enviar Email", command=enviar).pack()
    tk.Button(root, text="Voltar", command=lambda: telas.login.abrir_tela_login(root)).pack()

def limpar_janela(root):
    for widget in root.winfo_children():
        widget.destroy()