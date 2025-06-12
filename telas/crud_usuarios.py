from telas.utils_gui import limpar_janela
import tkinter as tk
from tkinter import messagebox
from database import get_users, delete_user
import telas.cadastro
from telas.editar_usuario import abrir_tela_editar
import telas.login

def abrir_tela_crud(root):
    limpar_janela(root)

    tk.Label(root, text="Usuários Cadastrados").pack()

    usuarios = get_users()
    for user in usuarios:
        tk.Label(root, text=f"{user[0]} - {user[1]} - {user[2]}").pack()

    tk.Label(root, text="ID do usuário para editar/excluir").pack()
    id_entry = tk.Entry(root)
    id_entry.pack()

    tk.Button(root, text="Adicionar", command=lambda: telas.cadastro.abrir_tela_cadastro(root)).pack()
    tk.Button(root, text="Editar", command=lambda: abrir_tela_editar(root, int(id_entry.get()))).pack()
    tk.Button(root, text="Excluir", command=lambda: excluir_usuario(root, int(id_entry.get()))).pack()
    tk.Button(root, text="Sair", command=lambda: telas.login.abrir_tela_login(root)).pack()

def excluir_usuario(root, user_id):
    if messagebox.askyesno("Confirmar", "Deseja realmente excluir este usuário?"):
        delete_user(user_id)
        messagebox.showinfo("Sucesso", "Usuário excluído.")
        telas.crud_usuarios.abrir_tela_crud(root)

def limpar_janela(root):
    for widget in root.winfo_children():
        widget.destroy()