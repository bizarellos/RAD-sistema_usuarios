import tkinter as tk
from telas.login import abrir_tela_login

def main():
    root = tk.Tk()
    root.title("Sistema de Usuários")
    root.geometry("400x400")
    abrir_tela_login(root)
    root.mainloop()

if __name__ == "__main__":
    main()