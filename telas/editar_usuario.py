from telas.utils_gui import limpar_janela
import tkinter as tk
from tkinter import messagebox
from database import get_user_by_id, update_user
import telas.crud_usuarios

def abrir_tela_editar(root, user_id):
    limpar_janela(root)

    user = get_user_by_id(user_id)
    if not user:
        messagebox.showerror("Erro", "Usuário não encontrado.")
        telas.crud_usuarios.abrir_tela_crud(root)
        return

    tk.Label(root, text="Editar Usuário").pack()
    tk.Label(root, text="Nome").pack()
    nome = tk.Entry(root)
    nome.insert(0, user[1])
    nome.pack()

    tk.Label(root, text="Email").pack()
    email = tk.Entry(root)
    email.insert(0, user[2])
    email.pack()

    def salvar():
        update_user(user_id, nome.get(), email.get())
        messagebox.showinfo("Sucesso", "Usuário atualizado.")
        telas.crud_usuarios.abrir_tela_crud(root)

    tk.Button(root, text="Salvar", command=salvar).pack()
    tk.Button(root, text="Voltar", command=lambda: telas.crud_usuarios.abrir_tela_crud(root)).pack()

def limpar_janela(root):
    for widget in root.winfo_children():
        widget.destroy()