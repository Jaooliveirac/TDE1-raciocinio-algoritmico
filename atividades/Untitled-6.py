import tkinter as tk
from tkinter import simpledialog, messagebox

# Configuração do tema do tkinter
tk.Tk().tk_setPalette(background='lightblue')
# Função para fazer as perguntas em etapas
def perguntas_em_etapas():
    # Etapa 1: Pergunta o nome do usuário
    nome1 = simpledialog.askstring("Pergunta para a gatinha", "Digite seu nome:")
    
    # Se o usuário cancelar a entrada, encerramos o programa
    if not nome1:
        return
    
    # Etapa 2: Pergunta o nome do namorado
    nome2 = simpledialog.askstring("Pergunta 2", f"Oi {nome1}, agora digite o nome do seu namorado:")
    
    # Se o usuário cancelar a entrada, encerramos o programa
    if not nome2:
        return

    # Etapa 3: Mostra a mensagem de resposta
    messagebox.showinfo("Resultado", f"Hum, eu conheço o {nome2} e ele é muito legal!\nVocês formam um belo casal! 😊")

# Configuração da janela principal
root = tk.Tk()
root.withdraw()  # Esconde a janela principal, só queremos as caixas de diálogo

# Executa a função de perguntas
perguntas_em_etapas()

# Encerra o programa
root.quit()
