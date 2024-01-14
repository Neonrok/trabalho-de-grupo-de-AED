import tkinter as tk
from tkinter import messagebox

def criar_botao(variavel):
    # Função associada ao botão
    def on_button_click():
        messagebox.showinfo("Botão Clicado", f"Você clicou no botão associado à variável: {variavel}")

    # Criação do botão
    botao = tk.Button(root, text=f"Botão {variavel}", command=on_button_click)
    botao.pack(pady=5)

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de Botões com Variáveis")

# Criar dois botões, cada um associado a uma variável diferente
criar_botao("A")
criar_botao("B")

# Iniciar o loop principal
root.mainloop()