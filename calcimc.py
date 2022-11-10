import tkinter as tk
from tkinter import ttk
from tkinter import END

janela = tk.Tk()
janela.title("Cálculo do IMC - Índice de Massa Corporal")
janela.geometry("500x300")


label_nome = ttk.Label(janela, text="Nome do Paciente: ")
label_nome.grid(row = 0, column= 0, padx= 5, pady= 5, sticky=tk.W)
nome = ttk.Entry(janela, width= 50)
nome.grid(row = 0, column= 1, padx= 5, pady= 5)


label_endereco = ttk.Label(janela, text="Endereço Completo: ")
label_endereco.grid(row = 1, column= 0, padx= 5, pady= 5, sticky=tk.W)
endereco = ttk.Entry(janela, width= 50)
endereco.grid(row = 1, column= 1, padx= 5, pady= 5)

label_altura = ttk.Label(janela, text="Altura(cm): ")
label_altura.grid(row = 2, column= 0, padx= 5, pady= 5, sticky=tk.W)
altura = ttk.Entry(janela, width= 20)
altura.grid(row = 2, column= 1, padx= 5, pady= 5, sticky=tk.W)

label_peso = ttk.Label(janela, text="Peso(Kg): ")
label_peso.grid(row = 3, column= 0, padx= 5, pady= 5, sticky=tk.W)
peso = ttk.Entry(janela, width= 20)
peso.grid(row = 3, column= 1, padx= 5, pady= 5, sticky=tk.W)

def calc():
    n = nome.get()
    e = endereco.get()
    a = int(altura.get())
    p = int(peso.get())
    a = a * 0.01
    imc = p / (a * a)

    if imc < 18.5:
        label_resultado = ttk.Label(janela, text= f"{n}\n{e}\nSeu IMC é {imc:.1f}.\nBaixo Peso.", width= 28)
        label_resultado.grid(row = 2, column = 1, stick=tk.E)
        label_resultado.config(background="white")
    elif imc >= 18.5 and imc <= 24.99:
        label_resultado = ttk.Label(janela, text= f"{n}\n{e}\nSeu IMC é {imc:.1f}.\nPeso Normal.", width= 28)
        label_resultado.grid(row = 2, column = 1, stick=tk.E)
        label_resultado.config(background="white")
    elif imc >= 25 and imc <= 29.99:
        label_resultado = ttk.Label(janela, text= f"{n}\n{e}\nSeu IMC é {imc:.1f}.\nSobrepeso.", width= 28)
        label_resultado.grid(row = 2, column = 1, stick=tk.E)
        label_resultado.config(background="white")
    else:
        label_resultado = ttk.Label(janela, text= f"{n}\n{e}\nSeu IMC é {imc:.1f}.\nObesidade.", width= 28)
        label_resultado.grid(row = 2, column = 1, stick=tk.E)
        label_resultado.config(background="white")

def reiniciar():
    nome.delete(0, END)
    endereco.delete(0, END)
    altura.delete(0, END)
    peso.delete(0, END)
    
def sair():
    janela.destroy()


b = ttk.Button(janela, text="Calcular", command=calc)
b.grid(row = 5, column = 1, sticky=tk.W)

r = ttk.Button(janela, text="Reiniciar", command=reiniciar)
r.grid(row = 5, column = 1, sticky=tk.NS)

s = ttk.Button(janela, text="Sair", command=sair)
s.grid(row = 5, column = 1, sticky=tk.E)



janela.mainloop()