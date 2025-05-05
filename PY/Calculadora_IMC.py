import tkinter as tk

def calcular():
    peso = float(Peso_entry.get())
    altura = float(Altura_entry.get()) / 100
    imc = peso / (altura ** 2)
    nome = str(Nome_entry.get())

    if imc < 18.5:
        return imc_label.config(text=f'{nome} seu IMC é: {imc:.2f}, Você está Abaixo do peso')
    elif 18.5 <= imc < 24.9:
        return imc_label.config(text=f'{nome} seu IMC é: {imc:.2f}, Você está com peso adequado')
    elif 25 <= imc < 29.9:
        return imc_label.config(text=f'{nome} seu IMC é: {imc:.2f}, Você está com Sobrepeso')
    elif 30 <= imc < 34.9:
        return imc_label.config(text=f'{nome} seu IMC é: {imc:.2f}, Você está com Obesidade I')
    elif 35 <= imc < 39.9:
        return imc_label.config(text=f'{nome} seu IMC é: {imc:.2f}, Você está com Obesidade II')
    elif 40 <= imc:
        return imc_label.config(text=f'{nome} seu IMC é: {imc:.2f}, Você está com Obesidade III')

# tela
tela = tk.Tk()
tela.title("Calculadora IMC")
tela.configure(bg="#1A1A19")

# Título
titulo = tk.Label(tela, text="CALCULE SEU IMC", fg="#2973B2", font=("DinaRemasterII 22"), bg="#1A1A19")
titulo.grid(row=0, column=0, columnspan=2, pady=20)

# Nome
Nome_label = tk.Label(tela, text="Digite Seu Nome", fg="#2973B2", font=("DinaRemasterII 15"), bg="#1A1A19")
Nome_label.grid(row=1, column=0, sticky="W", pady="5", padx="5")

Nome_entry = tk.Entry(tela, font=("DinaRemasterII 15"), bg="#FBFBFB")
Nome_entry.grid(row=1, column=1, sticky="W", pady="5", padx="5")

# Peso
Peso_label = tk.Label(tela, text="Digite Seu Peso(kg)", fg="#2973B2", font=("DinaRemasterII 15"), bg="#1A1A19")
Peso_label.grid(row=2, column=0, sticky="W", pady="5", padx="5")

Peso_entry = tk.Entry(tela, font=("DinaRemasterII 15"), bg="#FBFBFB")
Peso_entry.grid(row=2, column=1, sticky="W", pady="5", padx="5")

# Altura
Altura_label = tk.Label(tela, text="Digite Sua Altura(cm)", fg="#2973B2", font=("DinaRemasterII 15"), bg="#1A1A19")
Altura_label.grid(row=3, column=0, sticky="W", pady="5", padx="5")

Altura_entry = tk.Entry(tela, font=("DinaRemasterII 15"), bg="#FBFBFB")
Altura_entry.grid(row=3, column=1, sticky="W", pady="5", padx="5")

# Botão
botao = tk.Button(tela, text="Calcular", fg="#2973B2", command=calcular)
botao.grid(row=4, column=0, columnspan=2, sticky="we", pady="5", padx="5")


imc_label = tk.Label(tela, text=" ", fg="#2973B2", font=("DinaRemasterII", 15), bg="#1A1A19")
imc_label.grid(row=5, column=0, columnspan=2, sticky="w")

Peso_entry.focus()
tk.mainloop()