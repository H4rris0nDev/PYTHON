codigo fonte tv - site

FUNÇÃO -
def dividir(num1, num2):
    resultado = num1/num2
    print(f"Resultado: {resultado}")

dividir(num2=5, num1=100)



import tkinter as tk

def calcular():
    celsius = float(entrada_entry.get())
    Fahrenheit = celsius/5 * 9 + 32
    kelvin = celsius + 273

    Fahrenheit_Label.configure(text=f"Fahrenheit: {Fahrenheit}")
    Kelvin_Label.configure(text=f"Kelvin: {kelvin}")


tela = tk.Tk()
tela.title("Conversor de Temperatura")
tela.configure(bg="#EEEEEE")

titulo = tk.Label(tela, text ="CONVERSOR TEMPERATURA", fg="#8E1616", font=("DinaRemasterII 22"), bg="#EEEEEE") 
#TITULO escrever na tela = label.
titulo.grid(row=0, column=0, columnspan=2, pady=20)
#row linha. columns coluna.

#TEXTOS
entrada_label = tk.Label (tela, text="Temperatura em C°", fg="#8E1616", font=("DinaRemasterII 15"), bg="#EEEEEE")
entrada_label.grid(row=1, column=0, sticky="W", pady="5", padx="5")

entrada_entry = tk.Entry(tela, font=("DinaRemasterII 15"), bg="#EEEEEE")
entrada_entry.grid(row=1, column=1, sticky="W", pady="5", padx="5")

Fahrenheit_Label = tk.Label(tela, text="Fahrenheit: 0.0°F", fg="#8E1616", font= ("DinaRemasterII 15"), bg="#EEEEEE")
Fahrenheit_Label.grid(row=2, column=0, columnspan=2, sticky="W", pady="5", padx="5")

Kelvin_Label = tk.Label(tela, text="Kelvin: 0.0K", fg="#8E1616", font= ("DinaRemasterII 15"), bg="#EEEEEE")
Kelvin_Label.grid(row=3, column=0, columnspan=2, sticky="W", pady="5", padx="5")

botao = tk.Button(tela, text="Converter", fg= "#D84040", command=calcular)
botao.grid(row=4, column=0, columnspan=2, sticky="we", pady="5", padx="5")

entrada_entry.focus()
tk.mainloop()