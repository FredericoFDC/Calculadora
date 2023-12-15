import tkinter as tk
from tkinter import messagebox

def abrir_janela_funcao():
    funcao_escolhida = var_funcao.get()

    if funcao_escolhida:
        # Esconder a janela de seleção
        janela_selecao.withdraw()

        # Criar a janela correspondente à função escolhida
        janela_funcao = tk.Toplevel(janela_selecao)
        janela_funcao.title(f"Executar {funcao_escolhida.capitalize()}")
        janela_funcao.geometry("400x400")

        # Restante do código para a janela correspondente à função escolhida
        tk.Label(janela_funcao, text="Insira o primeiro valor:").pack()
        entry_valor1 = tk.Entry(janela_funcao, width=10)
        entry_valor1.pack(pady=10)

        tk.Label(janela_funcao, text="Insira o segundo valor:").pack()
        entry_valor2 = tk.Entry(janela_funcao, width=10)
        entry_valor2.pack(pady=10)

        # Botão para executar a função
        botao_executar = tk.Button(janela_funcao, text=f"Executar {funcao_escolhida.capitalize()}", command=lambda: executar_funcao(funcao_escolhida, entry_valor1, entry_valor2, label_resultado, janela_selecao))
        botao_executar.pack(pady=20)

        # Botão para voltar para o início
        botao_voltar = tk.Button(janela_funcao, text="Voltar para o início", command=lambda: voltar_para_inicio(janela_selecao, janela_funcao))
        botao_voltar.pack(pady=20)

        # Rótulo para exibir resultados
        label_resultado = tk.Label(janela_funcao, text="")
        label_resultado.pack(pady=20)

    else:
        messagebox.showwarning("Aviso", "Escolha uma função antes de confirmar.")

def executar_funcao(funcao, entry_valor1, entry_valor2, label_resultado, janela_selecao):
    try:
        valor1 = float(entry_valor1.get())
        valor2 = float(entry_valor2.get())

        if funcao == "somar":
            resultado = valor1 + valor2
        elif funcao == "subtrair":
            resultado = valor1 - valor2
        elif funcao == "multiplicar":
            resultado = valor1 * valor2
        elif funcao == "dividir":
            if valor2 != 0:
                resultado = valor1 / valor2
            else:
                messagebox.showerror("Erro", "Divisão por zero.")
                return

        # Formatando o resultado como um número inteiro, se possível
        resultado_formatado = int(resultado) if resultado.is_integer() else resultado

        # Configurando o texto do rótulo com a formatação
        label_resultado.config(text=f"Resultado da {funcao}: {resultado_formatado}", justify='center', font=("Arial", 14), padx=10)

    except ValueError:
        # Tratar erro se os valores inseridos não forem números
        label_resultado.config(text="Erro: Insira valores válidos.")

def voltar_para_inicio(janela_selecao, janela_funcao):
    # Destruir a segunda janela
    janela_funcao.destroy()

    # Exibir novamente a janela de seleção
    janela_selecao.deiconify()

# Criação da janela de seleção
janela_selecao = tk.Tk()
janela_selecao.title("Seleção de Função")
janela_selecao.geometry("300x200")

label_instrucao = tk.Label(janela_selecao, text="Escolha uma função:")
label_instrucao.pack(pady=10)

var_funcao = tk.StringVar()

opcoes_funcao = ["somar", "subtrair", "multiplicar", "dividir"]

for opcao in opcoes_funcao:
    radio_opcao = tk.Radiobutton(janela_selecao, text=opcao.capitalize(), variable=var_funcao, value=opcao)
    radio_opcao.pack()

botao_confirmar = tk.Button(janela_selecao, text="Confirmar", command=abrir_janela_funcao)
botao_confirmar.pack(pady=20)

# Iniciar o loop principal da interface gráfica da janela de seleção
janela_selecao.mainloop()
