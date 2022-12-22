import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry('480x360')

ventana.title('Calculadora IMC (indice masa corporal)')

resultado= tk.messagebox

font = 'Godzilla'

t1 = tk.Label(ventana, text= 'Ingresa tu peso en KG',font=font)
t1.pack(pady=15)
peso = tk.Entry(font=font,justify='center')
peso.pack(pady=10)
t2 = tk.Label(ventana, text='Ingresa tu altura en CM', font=font)
t2.pack(pady=15)
altura = tk.Entry(font=font,justify='center')
altura.pack(pady=10)
def imc():
    peso_valor= int(peso.get())
    altura_valor= int(altura.get())
    imc = peso_valor/(altura_valor/100)**2

    if imc < 18.5:
        resultado.showinfo(message= f'Tu imc es {round(imc,1)}, tienes peso muy bajo',title='Resultado')
  
        
    elif imc >= 18.5 and imc <=24.9:
        resultado.showinfo(message= f'Tu imc es {round(imc,1)}, tienes un peso saludable',title='Resultado')


    elif imc >= 25 and imc <=29.9:
        resultado.showinfo(message= f'Tu imc es {round(imc,1)}, tienes sobrepeso', title='Resultado')


    elif imc < 30:
        tk.Label(ventana2,text= f'Tu imc es {round(imc,1)}, tienes obesidad',font='Arial 15').pack(pady=10)


peso.focus_set()

calcular = tk.Button(ventana, command= imc, text='calcular', font=font)
calcular.pack(pady=20)

ventana.mainloop()