# telas/utils_gui.py

def limpar_janela(root):
    for widget in root.winfo_children():
        widget.destroy()
